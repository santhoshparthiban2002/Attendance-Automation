from django.shortcuts import render
from django.http import HttpResponse
import cv2
import mediapipe as mp
import time
import face_recognition
import numpy as np
from django.http import StreamingHttpResponse
from accounts.models import student,face
from datetime import date,datetime
import datetime
from attendence.models import attendance_record
import pdfkit



def attendance():
    faces = face.objects.all()
    encodelistknown =[]
    stdids = []
    
    for f in faces:
        a=[f.encode]
        encodelistknown.append(np.array([np.fromstring(a[0][1:-1], sep=' ')])[0])
        stdids.append(f.user.roll)
    print(encodelistknown)
    mpFaceDetection = mp.solutions.face_detection
    faceDetection = mpFaceDetection.FaceDetection(0.75)
    cap = cv2.VideoCapture(0)
    pTime = 0

    while True:
        success, img = cap.read()
        if not success:
            break
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(imgRGB)
        encodecuurframe = []
        facecurrframe = []
        # Process each face detection result
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(img, bbox, (255, 0, 255), 2)
                cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                            (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                            2, (255, 0, 255), 2)
            faceloc = face_recognition.face_locations(imgRGB)
            print(faceloc)
            if len(faceloc) > 0:
                enfoce = face_recognition.face_encodings(imgRGB, faceloc)[0]
                encodecuurframe.append(enfoce)
                facecurrframe.append(faceloc)
        for enfoce,faceloc in zip(encodecuurframe,facecurrframe):
            matches = face_recognition.compare_faces(encodelistknown, enfoce, tolerance=0.4)
            facedis = face_recognition.face_distance(encodelistknown, enfoce)
            matchindex=np.argmin(facedis)
            if matches[matchindex]:
                students = student.objects.filter(roll=stdids[matchindex])
                if students.exists():
                    student_obj = students.first()
                    attendance_exists = attendance_record.objects.filter(user=student_obj, date=date.today()).exists()
                    if not attendance_exists:
                        now = datetime.datetime.now() # Get the current datetime
                        morning_time = datetime.time(9, 30)  # Set the morning time to 9:30 AM
                        if now.time() < morning_time:
                            status = 'PRESENT'
                        else:
                            status = 'LATE'
                        attendance = attendance_record(user=student_obj, date=date.today(), datetime=now, status=status)
                        attendance.save()


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 2)


        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()
    
def stream(request):
    return StreamingHttpResponse(attendance(), content_type='multipart/x-mixed-replace; boundary=frame')


def my_view(request):
    return render(request, 'stream/a1.html')



from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def student_attendance_pdf(request,username):

    template_path = 'pdfgenrator/student_record.html'

    context = {'username': username}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




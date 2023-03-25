from django.shortcuts import render
from django.http import HttpResponse
import cv2
import mediapipe as mp
import time
import face_recognition
import numpy as np
from django.http import StreamingHttpResponse
from accounts.models import student,face
from datetime import date
from attendence.models import attendence_1_year
from course.models import course_period
def attendance():
    faces = face.objects.all()
    encodelistknown =[]
    stdids = []
    for f in faces:
        a=[f.encode]
        encodelistknown.append(np.array([np.fromstring(a[0][1:-1], sep=' ')])[0])
        stdids.append(f.user.roll)
    mpFaceDetection = mp.solutions.face_detection
    faceDetection = mpFaceDetection.FaceDetection(0.75)
    cap = cv2.VideoCapture(0)
    pTime = 0

    while True:
        # Read a frame from the video capture
        success, img = cap.read()
        if not success:
            break
        # Convert the frame to RGB for face recognition
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Detect faces in the frame using the face detection model
        results = faceDetection.process(imgRGB)
        # Create an empty list to store the encodings of the faces detected in the current frame
        encodecuurframe = []
        facecurrframe = []
        # Process each face detection result
        if results.detections:
            for detection in results.detections:
                # Get the bounding box of the face
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)

                # Draw a rectangle around the face
                cv2.rectangle(img, bbox, (255, 0, 255), 2)

                # Add the face detection confidence score as text
                cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                            (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                            2, (255, 0, 255), 2)
            faceloc = face_recognition.face_locations(imgRGB)
            if len(faceloc) > 0:
                enfoce = face_recognition.face_encodings(imgRGB, faceloc)[0]
                encodecuurframe.append(enfoce)
                facecurrframe.append(faceloc)
    
    # Compare the current face encodings with the known face encodings
        for enfoce,faceloc in zip(encodecuurframe,facecurrframe):
            matches = face_recognition.compare_faces(encodelistknown, enfoce)
            facedis = face_recognition.face_distance(encodelistknown, enfoce)
            matchindex=np.argmin(facedis)
            if matches[matchindex]:
                students = student.objects.filter(roll=stdids[matchindex])
                if students.exists():
                    student_obj = students.first()
                    attendance_exists = attendence_1_year.objects.filter(user=student_obj, date=date.today()).exists()
                    if not attendance_exists:
                        attendance = attendence_1_year(user=student_obj, date=date.today(), status='present')
                        attendance.save()
        # Add the FPS as text
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

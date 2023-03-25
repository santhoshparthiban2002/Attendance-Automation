from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from accounts.models import student
from accounts.models import face
import face_recognition
import cv2
from django.core.exceptions import ValidationError

@receiver(post_save, sender=student)
def my_receiver_function(sender, instance, created, **kwargs):
    if created:
        image_file = instance.photo.path
        role = instance.pk
        img = cv2.imread(image_file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(img)
        if len(face_encodings) > 0:
            encode = face_encodings[0]
            user = student.objects.get(pk=role)
            users = face(user=user, image=img, encode=encode)
            users.save()

    else:
        try:
            users = face.objects.get(user=instance.pk)
            image_file = instance.photo.path
            img = cv2.imread(image_file)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_encodings = face_recognition.face_encodings(img)
            if len(face_encodings) > 0:
                encode = face_encodings[0]
                users.image = img
                users.encode = encode
                users.save()
        except face.DoesNotExist:
            pass

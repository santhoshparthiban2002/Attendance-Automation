from django.db import models
import os
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

def employee_image_rename(instance, filename):
    upload_to = 'images/employee'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.user, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(null=True,upload_to=employee_image_rename)
    name=models.CharField(max_length=100,null=True)
    roll=models.CharField(max_length=100,primary_key=True)
    dob=models.DateField(null=True)
    department=models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    mobile=models.BigIntegerField(null=True)
    def __str__(self):
        return f'{self.name} - {self.department}'
    
@receiver(post_delete, sender=employee)
def auto_delete_employee_photo_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


def student_image_rename(instance, filename):
    upload_to = 'images/student'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.user, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to=student_image_rename,null=True)
    name=models.CharField(max_length=100,null=True)
    roll=models.CharField(max_length=100,primary_key=True)
    degree=models.CharField(max_length=100,null=True)
    branch=models.CharField(max_length=100,null=True)
    batch=models.IntegerField(null=True)
    year=models.CharField(max_length=2,null=True)
    semester=models.CharField(max_length=2,null=True)
    dob=models.DateField(null=True)
    mobile=models.BigIntegerField(null=True)
    parent_mobile=models.BigIntegerField(null=True)
    email=models.EmailField(max_length=100,null=True)
    def __str__(self):
        return f'{self.roll}'
    
@receiver(post_delete, sender=student)
def auto_delete_employee_photo_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

class face(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE)
    image = models.TextField(null=True)
    encode = models.TextField(null=True)
    def __str__(self):
        return f'{self.user.name} - {self.user.roll}'
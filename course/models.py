from django.db import models
from accounts.models import student

class course_period(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    batch=models.IntegerField(null=True)
    degree=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=2,null=True)
    semester=models.CharField(max_length=2,null=True)
    start=models.DateField(null=True)
    end=models.DateField(null=True)
    class Meta:
        unique_together = [('batch', 'degree','year','semester')]
    def __str__(self):
        return f'{self.name}'


class holidays(models.Model):
    batch=models.IntegerField(null=True)
    reason=models.CharField(max_length=100,null=True)
    date=models.DateField(null=True)
    class Meta:
        unique_together = [('batch','date')]
    def __str__(self):
        return f'{self.reason} - {self.date}'  
    
class enrollment(models.Model):
    enroll = models.CharField(max_length=100,primary_key=True)
    user =  models.ForeignKey(student, on_delete=models.CASCADE)
    courses = models.ManyToManyField(course_period)
    def get_courses_display(self):
        return ', '.join(str(course) for course in self.courses.all())

    def __str__(self):
        return f'{self.enroll} - {self.get_courses_display()}'

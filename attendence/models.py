from django.db import models
from accounts.models import student
from course.models import course_period
 
class attendence_1_year(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    status=models.CharField(max_length=100,null=True)
    class Meta:
        unique_together = [('user','date')]
    def __str__(self):
        return f'{self.user.name} - {self.date} - {self.status}'
     
class attendence_2_year(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE)
    course_period = models.ForeignKey(course_period, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    status=models.CharField(max_length=100,null=True)
    class Meta:
        unique_together = [('user', 'course_period','date')]
    def __str__(self):
        return f'{self.user.name} - {self.date} - {self.status}'

class attendence_3_year(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE)
    course_period = models.ForeignKey(course_period, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    status=models.CharField(max_length=100,null=True)
    class Meta:
        unique_together = [('user', 'course_period','date')]
    def __str__(self):
        return f'{self.user.name} - {self.date} - {self.status}'

class attendence_4_year(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE)
    course_period = models.ForeignKey(course_period, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    status=models.CharField(max_length=100,null=True)
    class Meta:
        unique_together = [('user', 'course_period','date')]
    def __str__(self):
        return f'{self.user.name} - {self.date} - {self.status}'
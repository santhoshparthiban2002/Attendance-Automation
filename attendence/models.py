from django.db import models
from accounts.models import student

 
class attendance_record(models.Model):
    user = models.ForeignKey(student, on_delete=models.CASCADE)
    date=models.DateField(null=True)
    datetime = models.DateTimeField(null=True)
    status=models.CharField(max_length=100,null=True)
    class Meta:
        unique_together = [('user','date')]
    def __str__(self):
        return f'{self.user.name} - {self.date} - {self.status}'
     
   
from django.db import models


class course_period(models.Model):
    batch=models.IntegerField(null=True)
    degree=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=2,null=True)
    semester=models.CharField(max_length=2,null=True)
    start=models.DateField(null=True)
    end=models.DateField(null=True)
    def __str__(self):
        return f'{self.batch} - {self.year} - {self.degree} '

class holidays(models.Model):
    batch=models.IntegerField(null=True)
    reason=models.CharField(max_length=100,null=True)
    date=models.DateField(null=True)
    class Meta:
        unique_together = [('batch', 'reason','date')]
    def __str__(self):
        return f'{self.reason} - {self.date}'
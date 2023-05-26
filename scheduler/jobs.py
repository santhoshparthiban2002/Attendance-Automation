
from datetime import date,timedelta,datetime
from course.models import holidays,course_period
from accounts.models import student,User
from django.contrib.auth import get_user_model
from attendence.models import attendance_record
from datetime import date,datetime

def auto_detect_sundays():
   a=1
   year=datetime.now().year
   d = date(year, 1, 1)                 
   d += timedelta(days = 6 - d.weekday())
   while d.year == year:
      dates=holidays()
      dates.batch=datetime.now().year
      dates.reason="Sunday - "+str(a)
      dates.date=d
      dates.save()
      a+=1
      d += timedelta(days = 7)

def auto_delete():
   year=datetime.now().year-6
   User=get_user_model()
   students=student.objects.filter(batch__lte=year)
   for i in students:
      user=i.user
      i.delete()
      user.delete()
   holidays.objects.filter(batch__lte=year).delete()
   course_period.objects.filter(batch__lte=year).delete()


def attendance_absent():
   students = student.objects.all()
   for i in students:
      attendance, created = attendance_record.objects.get_or_create(user=i, date=date.today())
      if created:
         attendance.datetime=datetime.now()
         attendance.status="ABSENT"
         attendance.save()
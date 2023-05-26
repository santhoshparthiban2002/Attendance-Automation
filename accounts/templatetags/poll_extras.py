from accounts.models import *
from course.models import *
from attendence.models import *
from django import template
from datetime import *
import datetime
register = template.Library()

@register.simple_tag
def studentdata(user):
    print(user)
    datas = student.objects.filter(roll=user).get()
    return datas 

@register.simple_tag
def print_date(x):
    return x.strftime('%d-%m-%Y')

@register.simple_tag
def print_datetime(x):
    return x.strftime('%H:%M:%S')


@register.simple_tag
def no_of_days(x):
    courses = course_period.objects.get(name=x)
    start_date = courses.start
    end_date = courses.end
    holidays_list = holidays.objects.values_list('date', flat=True).distinct()

    delta = end_date - start_date
    num_days = delta.days + 1

    num_working_days = 0
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        if current_date not in holidays_list and current_date<=date.today():
            num_working_days += 1
    return num_working_days

@register.simple_tag
def no_of_days_present(x,y):
    courses = course_period.objects.get(name=x)
    start_date = courses.start
    end_date = courses.end
    holidays_list = holidays.objects.values_list('date', flat=True).distinct()
    students = student.objects.filter(roll=y).get()
    attendence_data = attendance_record.objects.filter(user=students,status="PRESENT").values_list('date', flat=True).distinct()
    delta = end_date - start_date
    num_days = delta.days + 1
    count = 0
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        if current_date in attendence_data  :
            count += 1
    return count

@register.simple_tag
def no_of_days_late(x,y):
    courses = course_period.objects.get(name=x)
    start_date = courses.start
    end_date = courses.end
    holidays_list = holidays.objects.values_list('date', flat=True).distinct()
    students = student.objects.filter(roll=y).get()
    attendence_data = attendance_record.objects.filter(user=students,status="LATE").values_list('date', flat=True).distinct()
    delta = end_date - start_date
    num_days = delta.days + 1
    count = 0
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        if current_date in attendence_data  :
            count += 1
    return count



@register.simple_tag
def no_of_days_absent(x,y):
    courses = course_period.objects.get(name=x)
    start_date = courses.start
    end_date = courses.end
    holidays_list = holidays.objects.values_list('date', flat=True).distinct()
    students = student.objects.filter(roll=y).get()
    attendence_data = attendance_record.objects.filter(user=students,status="ABSENT").values_list('date', flat=True).distinct()
    delta = end_date - start_date
    num_days = delta.days + 1
    count = 0
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        if current_date in attendence_data  :
            count += 1
    return count
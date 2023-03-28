from accounts.models import *
from course.models import *
from attendence.models import *
from django import template

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

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
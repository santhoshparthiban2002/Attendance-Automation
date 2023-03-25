from django.contrib import admin
from .models import course_period,holidays
# Register your models here.
admin.site.register(course_period)
admin.site.register(holidays)
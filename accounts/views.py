from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib.auth import*
from django.http import HttpResponse
from .models import *
# Create your views here.
@login_required
def home(request):
    if request.user.is_employee:
        return HttpResponse("staff")


def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
            if 'staff_submit' in request.POST:
                username = request.POST['staff_username']
                password = request.POST['staff_password']
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_employee:
                    auth.login(request, user)
                    return redirect('admins_dashboard')
                else:
                    messages.error(request, 'Invalid Staff Credentials')
                    return redirect('login')
            elif 'student_submit' in request.POST:
                username = request.POST['student_username']
                password = request.POST['student_password']
                user = auth.authenticate(username=username, password=password)
                if user is not None and  user.is_student:
                    auth.login(request, user)
                    print(user.username)
                    return redirect('student',username=user.username)
                else:
                    messages.error(request, 'Invalid Student Credentials')
                    return redirect('login')
    return render(request, 'login.html')

def staff_text(user):
    try:
        return user.is_authenticated and user.is_employee is True
    except User.DoesNotExist:
        return False
    
@user_passes_test(staff_text)
def admins(request):
    return render(request, 'admin/master.html')  

@user_passes_test(staff_text)
def admins_dashboard(request):

    return render(request, 'admin/dashboard.html') 
@user_passes_test(staff_text)
def admins_course(request):
    return render(request, 'admin/course.html') 

@user_passes_test(staff_text)

def admins_register(request):
    return render(request, 'admin/register.html') 

@user_passes_test(staff_text)
def admins_attendance(request):
    return render(request, 'admin/attendance.html') 

@user_passes_test(staff_text)
def admins_database(request):
    return render(request, 'admin/database.html') 


def student_text(user):
    try:
        return user.is_authenticated and user.is_student is True
    except User.DoesNotExist:
        return False
    
@user_passes_test(student_text)
def student_profile(request,username):
    profile=get_user_model().objects.filter(username=username).get()
    student_data=student.objects.filter(roll=profile).get()
    return render(request, 'student/main_student.html',{"profile":student_data})  

@user_passes_test(student_text)
def attendance_student(request,username):
    profile=get_user_model().objects.filter(username=username).get()
    student_data=student.objects.filter(roll=profile).get()
    return render(request, 'student/attendance_student.html',{"profile":student_data})  

@user_passes_test(student_text)
def leave_student(request,username):
    profile=get_user_model().objects.filter(username=username).get()
    student_data=student.objects.filter(roll=profile).get()
    return render(request, 'student/leave_student.html',{"profile":student_data})  
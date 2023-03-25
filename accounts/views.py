from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib.auth import*
from django.http import HttpResponse
from .models import *
from course.models import *
from attendence.models import *
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
    if request.method == 'POST':
        try:
            if 'studentregister' in request.POST:
                roll = request.POST['roll']
                dob = request.POST['name']
                is_student = True
                user = User.objects.create_user(username=roll,password=dob,is_student=is_student)
                user.save()
                students = student()
                students.user = user
                students.photo = request.FILES.get('studentimage')
                students.name  = request.POST['name']
                students.roll  = request.POST['roll']
                students.mobile  = request.POST['mobile']
                students.dob  = request.POST['dob']
                students.email  = request.POST['email']
                students.degree  = request.POST['degree']
                students.branch  = request.POST['branch']
                students.batch  = request.POST['batch']
                students.year  = request.POST['year']
                students.semester  = request.POST['semester']
                students.parent_mobile  = request.POST['parent']
                students.save()
                messages.success(request, 'Student registration successful.',extra_tags='success')
            if 'teacherregister' in request.POST:
                roll = request.POST['troll']
                dob = request.POST['tname']
                is_employee = True
                user = User.objects.create_user(username=roll,password=dob,is_employee=is_employee)
                user.save()
                teachers = employee()
                teachers.user = user
                teachers.photo = request.FILES.get('teacherimage')
                teachers.name  = request.POST['tname']
                teachers.roll  = request.POST['troll']
                teachers.mobile  = request.POST['tmobile']
                teachers.dob  = request.POST['tdob']
                #teachers.email  = request.POST['temail']
                #teachers.degree  = request.POST['tjd']
                teachers.department  = request.POST['tdept']
                teachers.designation  = request.POST['tdesig']
                teachers.save()
                messages.success(request, 'Teacher registration successful.',extra_tags='success')
        except Exception as e:
            messages.error(request, 'An error occurred while saving the data. Please try again later.',extra_tags='danger')
            # you can also log the error for debugging purposes
            print(e)
    return render(request, 'admin/register.html')

@user_passes_test(staff_text)
def admins_attendance(request):
    attendances=attendence_1_year.objects.all()
    students=student.objects.all()
    return render(request, 'admin/attendance.html',{"attendances":attendances,"students":students}) 

@user_passes_test(staff_text)
def admins_attendance_data(request):
    attendances=attendence_1_year.objects.all()
    students=student.objects.all()
    return render(request, 'admin/attendencedata.html',{"attendances":attendances,"students":students}) 

def update_attendance(request):
    if request.method == 'POST':
        roll = request.POST['attendance_roll']
        date = request.POST['attendance_date']
        status = request.POST['attendance_status']
        # Here you can update the database with the new values.
        person = attendence_1_year.objects.filter(user=roll, date=date).get()
        person.date = date
        person.status = status
        person.save()
        return redirect('admins_attendance')
    else:
        return render(request, 'admin/attendance.html')

@user_passes_test(staff_text)
def admins_database(request):
    employees=employee.objects.all()
    students=student.objects.all()
    courses = course_period.objects.all()
    return render(request, 'admin/database.html',{"employees":employees,"students":students,"courses":courses}) 


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
from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib.auth import*
from django.http import HttpResponse
from .models import *
from course.models import *
from attendence.models import *


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
    return render(request, 'admin/master.html', {'user': request.user})  


@user_passes_test(staff_text)
def admins_enrollment(request):
    if request.method == 'POST':
        if 'promotion' in request.POST:
            batch = request.POST['pbatch']
            degree  = request.POST['pdegree']
            branch  = request.POST['pbranch']
            year  = request.POST['pyear']
            semester  = request.POST['psemester']
            action  = request.POST['paction']
            try:
                students= student.objects.filter(batch=batch,degree=degree,branch=branch,year=year,semester=semester).all()
                for x in students:
                    print(students)
                    if action=="psemester" and int(x.semester) > 0:
                        x.semester = int(x.semester)+1
                    elif action=="pyear" and int(x.year) > 0:
                        x.year =int(x.year)+1
                    elif action=="dsemester" and int(x.semester) > 0:
                        x.semester =int(x.semester)-1
                    elif  action=="dyear" and int(x.year) > 0:
                        x.year =int(x.year)-1
                    else:
                        print("no")
                    x.save()
                messages.success(request, 'Course registration successful.',extra_tags='success')
            except Exception as e:
                messages.error(request, 'An error occurred while saving the data. Please try again later.',extra_tags='danger')
                print(e)
        
        if 'enrollment' in request.POST:
            batch = request.POST['ebatch']
            degree  = request.POST['edegree']
            branch  = request.POST['ebranch']
            year  = request.POST['eyear']
            semester  = request.POST['esemester']
            action  = request.POST['ecourse']
            students= student.objects.filter(batch=batch,degree=degree,branch=branch,year=year,semester=semester).all()
            print(action)
            courseid=course_period.objects.filter(name=action).get()
            print(courseid)

            for x in students:
                primarydata= str(x) +"-"+request.POST['edegree']+"-"+request.POST['ebranch']
                enrolls=enrollment()
                enrolls.user=x
                enrolls.enroll=primarydata
                enrolls.save()
                addcourse = enrollment.objects.filter(enroll=primarydata).get()
                addcourse.courses.add(courseid)
                addcourse.save()
    sstudents=student.objects.all()
    courses=course_period.objects.all()
    enrollments=enrollment.objects.all()
    return render(request, 'admin/enrollment.html',{"students":sstudents,"courses":courses,"enrollments":enrollments})  



@user_passes_test(staff_text)
def admins_dashboard(request):

    return render(request, 'admin/dashboard.html') 


@user_passes_test(staff_text)
def admins_profile(request,username):
    user = User.objects.get(username=username)
    student_profile = student.objects.filter(user=user).get()
    enrollments=enrollment.objects.filter(user=student_profile).get()
    data1 = student_profile.roll
    if data1!=username:
        student_profile.roll=username
        student_profile.save()

    if 'reset_password' in request.POST:
            try:
                user = User.objects.get(username=username)
                dates=student_profile.dob.strftime('%d-%m-%Y')
                user.set_password(str(dates))
                user.save()
                messages.success(request, 'Reset Password successful.',extra_tags='success')
            except Exception as e:
                    messages.error(request, 'An error occurred while Resetting the password. Please try again later.', extra_tags='danger')
                    print(e)
    if 'change_username' in request.POST:
        try:
            rolls = request.POST['roll']
            users = User.objects.get(username=username)
            if request.FILES.get('studentimage'):
                student_profile = student.objects.filter(user=users).get()
                student_profile.photo =  request.FILES.get('studentimage')
                student_profile.save()
            users.username = rolls
            users.save()
            messages.success(request, 'Record updated successfully.', extra_tags='success')
            return redirect('admins_profile',rolls)
        except Exception as e:
            messages.error(request, 'An error occurred while updating the record. Please try again later.', extra_tags='danger')
            print(e)
    if 'update_record' in request.POST:
        try:
            user = User.objects.get(username=username)
            students = student.objects.filter(user=user).get()
            students.name  = request.POST['name']
            students.mobile  = request.POST['mobile']
            students.dob  = request.POST['dob']
            students.email  = request.POST['email']
            students.degree  = request.POST['degree']
            students.branch  = request.POST['branch']
            students.batch  = request.POST['batch']
            students.year  = request.POST['year']
            students.semester  = request.POST['semester']
            students.parent_mobile  = request.POST['parent_mobile']
            students.save()
            messages.success(request, 'Record updated successfully.', extra_tags='success')
            return redirect('admins_profile',username)
        except Exception as e:
            messages.error(request, 'An error occurred while updating the record. Please try again later.', extra_tags='danger')
            print(e)  
    if 'delete_user' in request.POST:
        try:
            user = User.objects.get(username=username)
            user.delete()
            return redirect('admins_database')
        except Exception as e:
            messages.error(request, 'An error occurred while updating the record. Please try again later.', extra_tags='danger')
            print(e)  
        
    return render(request, 'admin/profile.html',{"student_profile":student_profile,"enrollments":enrollments}) 





@user_passes_test(staff_text)
def admins_course(request):
    if request.method == 'POST':
        try:
            if 'course' in request.POST:
                course = course_period()
                course.name = "SMIT-"+ str(request.POST['batch']) +"-" + str(request.POST['degree']) + "-"+ str(request.POST['year']) +"-" + str(request.POST['semester'])
                course.degree  = request.POST['degree']
                course.batch  = request.POST['batch']
                course.year  = request.POST['year']
                course.semester  = request.POST['semester']
                course.end  = request.POST['end']
                course.start  = request.POST['start']
                course.save()
                messages.success(request, 'Course registration successful.',extra_tags='success')
            if 'holiday' in request.POST:
                holiday = holidays()
                holiday.batch = request.POST['hyear']
                holiday.date = request.POST['date']
                holiday.reason  = request.POST['reason']
                holiday.save()
                messages.success(request, 'Holiday declaration successful.',extra_tags='success')
        except Exception as e:
            messages.error(request, 'An error occurred while saving the data. Please try again later.',extra_tags='danger')
            print(e)

        if 'update_course' in request.POST:
            try:
                name  = request.POST['name']
                course = course_period.objects.filter(name=name).get()
                course.start = request.POST['coursestart']
                course.end = request.POST['courseend']
                course.save()
                messages.success(request, 'Course update successful.',extra_tags='success')
            except Exception as e:
                messages.error(request, 'An error occurred while updation the data. Please try again later.',extra_tags='danger')
        if 'delete_course' in request.POST:
            try:
                name  = request.POST['name']
                course = course_period.objects.filter(name=name).get()
                course.delete()
                messages.success(request, 'Course deletion successful.',extra_tags='success')
            except Exception as e:
                messages.error(request, 'An error occurred while deleting the data. Please try again later.',extra_tags='danger')

        if 'update_holiday' in request.POST:
            try:
                holiday_year  = request.POST['hdyear']
                holiday_date  = request.POST['hddate']
                holiday_reason  = request.POST['hdreason']
                holiday = holidays.objects.filter(batch=holiday_year,date=holiday_date).get()
                holiday.batch=holiday_year
                holiday.date=holiday_date
                holiday.reason=holiday_reason
                holiday.save()
                messages.success(request, 'Holiday updation successful.',extra_tags='success')
            except Exception as e:
                messages.error(request, 'An error occurred while deleting the data. Please try again later.',extra_tags='danger')
                print(e)
        
        if 'delete_holiday' in request.POST:
            try:
                holiday_year  = request.POST['hdyear']
                holiday_date  = request.POST['hddate']
                holiday_reason  = request.POST['hdreason']
                holiday = holidays.objects.filter(batch=holiday_year,date=holiday_date).get()
                holiday.delete()
                messages.success(request, 'Holiday deletion successful.',extra_tags='success')
            except Exception as e:
                messages.error(request, 'An error occurred while deleting the data. Please try again later.',extra_tags='danger')
                print(e)









    leaves  = holidays.objects.all()
    courses = course_period.objects.all()
    return render(request, 'admin/course.html',{"courses":courses,"leaves":leaves}) 




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
                try:
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
                except Exception as e:
                      user.delete()
                      messages.error(request, 'An error occurred while saving the data. Please try again later.',extra_tags='danger')
            if 'teacherregister' in request.POST:
                roll = request.POST['troll']
                dob = request.POST['tname']
                is_employee = True
                user = User.objects.create_user(username=roll,password=dob,is_employee=is_employee)
                user.save()
                try:
                    teachers = employee()
                    teachers.user = user
                    teachers.photo = request.FILES.get('teacherimage')
                    teachers.name  = request.POST['tname']
                    teachers.roll  = request.POST['troll']
                    teachers.mobile  = request.POST['tmobile']
                    teachers.dob  = request.POST['tdob']
                    teachers.email  = request.POST['temail']
                    teachers.coordinate  = request.POST['tcoordinator']
                    teachers.department  = request.POST['tdept']
                    teachers.designation  = request.POST['tdesig']
                    teachers.save()
                    messages.success(request, 'Teacher registration successful.',extra_tags='success')
                except Exception as e:
                      username=request.POST['troll']
                      teacher_member = User.objects.get(username=username)
                      teacher_member.delete()
                      messages.error(request, 'An error occurred while saving the data. Please try again later.',extra_tags='danger')
                
        except Exception as e:
            messages.error(request, 'An error occurred while saving the data. Please try again later.',extra_tags='danger')
            # you can also log the error for debugging purposes
            print(e)
    return render(request, 'admin/register.html')

@user_passes_test(staff_text)
def admins_attendance(request):
    if request.method == 'POST':
        if 'update_attendance' in request.POST:
            try:
                roll = request.POST['attendance_roll']
                date = request.POST['attendance_date']
                status = request.POST['attendance_status']
                person = attendance_record.objects.filter(user=roll, date=date).get()
                person.date = date
                person.status = status
                person.save()
                messages.success(request, 'Attendance update successful.',extra_tags='success')
            except Exception as e:
                      messages.error(request, 'An error occurred while updating the data. Please try again later.',extra_tags='danger')
        if 'delete_attendance' in request.POST:
            try:
                roll = request.POST['attendance_roll']
                date = request.POST['attendance_date']
                status = request.POST['attendance_status']
                person = attendance_record.objects.filter(user=roll, date=date).get()
                person.delete()
                messages.success(request, 'Attendance Deletion successful.',extra_tags='success')
            except Exception as e:
                      messages.error(request, 'An error occurred while updating the data. Please try again later.',extra_tags='danger')
        if 'add_attendance' in request.POST:
            try:
                person = attendance_record()
                roll = request.POST['attendance_roll1']
                roll_data = student.objects.filter(roll=roll).get()
                person.user = roll_data
                person.date = request.POST['attendance_date1']
                person.status = request.POST['attendance_status1']
                person.save()
                messages.success(request, 'Attendance Deletion successful.',extra_tags='success')
            except IntegrityError as e:
                if 'unique constraint' in str(e).lower():
                    messages.error(request, 'Attendance data already exists for the selected student and date.', extra_tags='danger')
            except Exception as e:
                    messages.error(request, 'An error occurred while updating the data. Please try again later.', extra_tags='danger')
    attendances=attendance_record.objects.all()
    students=student.objects.all()
    return render(request, 'admin/attendance.html',{"attendances":attendances,"students":students}) 



@user_passes_test(staff_text)
def admins_database(request):
    employees=employee.objects.all()
    students=student.objects.all()
    courses = course_period.objects.all()
    leaves  = holidays.objects.all()
    return render(request, 'admin/database.html',{"employees":employees,"students":students,"courses":courses,"leaves":leaves}) 


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
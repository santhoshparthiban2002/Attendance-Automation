from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/', login,name="login"),
    path('home/', home,name="home"),
    path('logout/', logout,name="logout"),
    path('student/<str:username>', student_profile,name="student"),
    path('attendance/<str:username>', attendance_student,name="attendance_student"),
    path('leave/<str:username>', leave_student,name="leave_student"),
    path('admins/dashboard', admins_dashboard,name="admins_dashboard"),
    path('admins/register', admins_register,name="admins_register"),
    path('admins/database', admins_database,name="admins_database"),
    path('admins/course', admins_course,name="admins_course"),
    path('admins/attendance', admins_attendance,name="admins_attendance"),
    path('admins/attendance/data', admins_attendance_data,name="admins_attendance_data"),
     path('admins/update_attendance', update_attendance,name="update_attendance"),
]
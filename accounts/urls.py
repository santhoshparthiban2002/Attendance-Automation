from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/', login,name="login"),
    path('logout/', logout,name="logout"),
    path('student/<str:username>', student_profile,name="student"),
    path('attendance/<str:username>', attendance_student,name="attendance_student"),
    path('leave/<str:username>', leave_student,name="leave_student"),
    path('admins/', admins,name="admins"),
    path('admins/dashboard', admins_dashboard,name="admins_dashboard"),
    path('admins/register', admins_register,name="admins_register"),
    path('admins/database/', admins_database,name="admins_database"),
    path('admins/database/<str:username>', admins_profile,name="admins_profile"),
    path('admins/course', admins_course,name="admins_course"),
    path('admins/enrollment', admins_enrollment,name="admins_enrollment"),
    path('admins/attendance', admins_attendance,name="admins_attendance"),
 
]

from django.contrib import admin
from django.urls import path,include
from attendence.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('attendance/', stream,name="attendance"),
    path('student_attendance_pdf/<int:username>', student_attendance_pdf,name="student_attendance_pdf"),
    path('a/', my_view,name="my_view"),
    path('',include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
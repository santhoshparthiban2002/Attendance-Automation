from django.contrib import admin
from .models import User,student,employee,face
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('username','is_employee', 'is_student')
    fieldsets = (
        ('ACCOUNT', {
            'fields': ('username', 'password')
        }),
        ('Permissions', {
            'fields': (
                 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('ACCOUNT STATUS', {
            'fields': ('last_login', 'date_joined','is_active')
        }),
        ('USER TYPE', {
            'fields': ('is_student', 'is_employee')
        })
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(student)
admin.site.register(employee)
admin.site.register(face)

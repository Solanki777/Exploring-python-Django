from django.contrib import admin
from .models import *

# admin.site.register(Department)
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=["department_name","department_code"]

@admin.register(StudentID)
class StudentIDAdmin(admin.ModelAdmin):
    list_display=["student_id"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_name",
        "student_id",
        "department",
        "student_email",
        "student_age",
    ]
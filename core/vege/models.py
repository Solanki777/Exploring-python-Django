from django.db import models

# it is predefind user inputs like fist name , last naem , email , pass you can check in models  in abstract user in env file
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):

    user=models.ForeignKey(User , on_delete=models.SET_NULL, null=True , blank=True )
    receipe_name=models.CharField(max_length=100)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to="uploads")
    receipe_count=models.IntegerField(default=0)

class StudentID(models.Model):
    student_id=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.student_id


class Department(models.Model):
    department_name=models.CharField(max_length=100, unique=True)
    department_code=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.department_name
    
    class Meta:
        ordering=['department_name']
        verbose_name="Department"

class Student(models.Model):

    # if one deprt is delete the whole student related to deprtment data will also be deleted
    # here we use foreignkey which means here it private key but for student it is same for many students
    # Department is other model where it regerse the private key
    # to get data we use department.students.all() but if we use simple word like dept so we can done using the related_name 
    department=models.ForeignKey(Department,related_name="dept", on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID,related_name="studentid", on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    # now when use makes the object of this function and you whant show what to disply for project you can do this instead
    # def __str__(self):
    #     return self.student_name
    
    # used configure model behavior
    class Meta:
        # database store according to id in ascending order 
        ordering=['student_id']

        # how the object is shown in admin pannel 
        verbose_name="Student"




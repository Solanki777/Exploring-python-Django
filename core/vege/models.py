from django.db import models

class Department(models.Model):
    department_name=models.CharField(max_length=100, unique=True)
    department_code=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.department_name
    
class StudentID(models.Model):
    student_id=models.CharField(max_length=200 , unique= True)

    def __str__(self):
        return self.student_id

class Student(models.Model):
    department=models.ForeignKey(
        Department,
        related_name="dept",
        on_delete=models.CASCADE

    )
    student_id=models.OneToOneField(
        StudentID,
        related_name="studentid",
        on_delete=models.CASCADE
    )

    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    class Meta:
        ordering=['student_id']
        verbose_name="Student"

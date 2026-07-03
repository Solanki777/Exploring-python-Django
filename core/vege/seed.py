from faker import Faker
fake=Faker()
import random
from .models import *


def seed_db(n=10):
    
    try:
        departments = Department.objects.all()

        if not departments.exists():
            print("no department")
            return 
        
        for _ in range(n):
            department=random.choice(departments)
            student_id= f"STU - {random.randint(230430116119,23043011616129)} "
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(20,30)
            student_address=fake.address()

            student_id_obj= StudentID.objects.create(student_id = student_id)

            student_obj=Student.objects.create(
                department = department , 
                student_id = student_id_obj , 
                student_name = student_name , 
                student_email = student_email , 
                student_age = student_age , 
                student_address = student_address , 
            )

    except Exception as e:
        print(e)

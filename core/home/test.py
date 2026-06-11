from django.test import TestCase
from .models import Students

class StudentTest(TestCase):
    def test_gretting(self):
        student = Students(
            name="Urmila",
            age=17,
            email="urmila7@gmail.com",
            address="Banglore"
        )
        

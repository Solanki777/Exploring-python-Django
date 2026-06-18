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
from django.db import models

# Create your models here.
class Studnets(models.Model):


    # name should be length in 100 characters
    # id = models.AutoField() #django will automatticalyy add this field to track multiple models
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True 
    )
# after creating any model or doing any changes in the model schemas the you have to hit the command
class Product(models.Model):
    pass
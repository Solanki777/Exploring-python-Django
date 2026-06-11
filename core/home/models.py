from django.db import models

# Create your models here.
class Students(models.Model):


    # name should be length in 100 characters
    # id = models.AutoField() #django will automatticalyy add this field to track multiple models
    name = models.CharField(max_length=100,null=True, blank=True )
    age = models.IntegerField(null=True, blank=True )
    email = models.EmailField(null=True, blank=True )
    address = models.TextField(null=True, blank=True 
    )

    def greeting(self):
        return f"Hello {self.name}"
# after creating any model or doing any changes in the model schemas the you have to hit the command
class Product(models.Model):
    pass
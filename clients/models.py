from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=240, unique=True)
    tel_number = models.CharField(max_length=20)
    #Automatically set the field to the current date when the field is created
    joined_date = models.DateField(auto_now_add=True) 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

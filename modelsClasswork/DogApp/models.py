# this code allow the user to input their answers.
from django.db import models

# Create your models here.
class Dog(models.Model):
    name= models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    color= models.CharField(max_length=50)
    gender= models.CharField(max_length=20)

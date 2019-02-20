# this code allows the user to input their answers to the question given
from django.db import models

# Create your models here.
class Newbalance(models.Model):
    username=models.CharField(max_length=200)
    realname=models.CharField(max_length=200)
    accountNumber=models.IntegerField(default=0)
    balance=models.IntegerField(default=0)
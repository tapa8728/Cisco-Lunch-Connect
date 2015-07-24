import datetime
# Create your models here.
from django.db import models
from django.utils import timezone

#User table
class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    businessunit = models.CharField(max_length=30)


    


    

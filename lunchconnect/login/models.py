import datetime

from django.db import models
from django.utils import timezone

#User table
class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(default="invalid")
    designation = models.CharField(max_length=40)
    businessunit = models.CharField(max_length=30)

#--------------Appointment table---------------
# Used for both intern & Manager
class Appointment(models.Model):
 	manager_username = models.CharField(max_length=200)
 	intern_username = models.CharField(max_length=200, blank=True)
 	location = models.CharField(max_length=200, blank=True)
 	additionalinfo = models.CharField(max_length=200, blank=True)
 	booked = models.BooleanField(default=False)
 	starttime = models.TimeField(default="12:30")
 	endtime = models.TimeField(default="1:30")
 	date=models.DateField(default="2009-10-03")


    

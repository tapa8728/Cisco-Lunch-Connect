import datetime
# Create your models here.
from django.db import models
from django.utils import timezone

#Username table
class Username(models.Model):
    username_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.username_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



#Password table
class Password(models.Model):
    #one password per username
    username = models.ForeignKey(Username)
    password_text = models.CharField(max_length=20)
    def __unicode__(self):
        return self.password_text
    

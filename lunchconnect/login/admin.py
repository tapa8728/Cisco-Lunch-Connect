from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'firstname', 'lastname', 'designation', 'businessunit')

              
admin.site.register(User, UserAdmin) #regster the table and the function

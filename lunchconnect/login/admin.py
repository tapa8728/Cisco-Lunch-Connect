from django.contrib import admin

# Register your models here.
from .models import User, Appointment

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'firstname', 'lastname', 'designation', 'businessunit')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('manager_username', 'intern_username', 'location', 'additionalinfo', 'booked')

# Register the table and the function
admin.site.register(User, UserAdmin) 
admin.site.register(Appointment, AppointmentAdmin )

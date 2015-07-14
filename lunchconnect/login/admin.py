from django.contrib import admin

# Register your models here.
from .models import Username, Password


admin.site.register(Password)

class UsernameAdmin(admin.ModelAdmin):
    list_display = ('username_text', 'pub_date', 'was_published_recently')

              
admin.site.register(Username, UsernameAdmin)

# Application login/views
from django.conf.urls import url

from . import views

urlpatterns = [
    
    # ---------Login Page : Existing Users
    url(r'^$', views.login, name='login'),

    # -------- Sign up : 1st time users --------- just shows login page
    url(r'^signup/$', views.signup, name='signup'),

    # -------- Push Login Data-------
    url(r'^submitform/$', views.submitform, name="submitform"),

    # -------- Push Sign Up Data-------
    url(r'^save/$', views.save, name="save"),

    #--------- Add new slot - Managers ------
    url(r'^addslot/$', views.addslot, name="addslot"),

    #--------- Book Available Slot - Interns -------
    url(r'^(?P<appointment_id>[0-9]+)/$', views.bookslot, name="bookslot"),

    #--------- Delete Available Slot - Mannagers -------
    url(r'^delete/(?P<appointment_id>[0-9]+)/$', views.deleteslot, name="deleteslot"),

    #--------- Email Interns - Mannagers -------
    url(r'^email/(?P<appointment_id>[0-9]+)/$', views.emailintern, name="emailintern")

]
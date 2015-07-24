# Application login/views
from django.conf.urls import url

from . import views

urlpatterns = [
    # /login/
    #url(r'^$', views.index, name='index'),
    # /login/1/
    # ex: /login/5/signin/#url(r'^(?P<username_id>[0-9]+)/signin/$', views.signin, name='signin'),
    # ex: /login/5/signup/

    # ---------Login Page : Existing Users
    url(r'^$', views.login, name='login'),

    # -------- Sign up : 1st time users --------- just shows login page
    url(r'^signup/$', views.signup, name='signup'),

    # -------- Push Login Data-------
    url(r'^submitform/$', views.submitform, name="submitform"),

    # -------- Push Sign Up Data-------
    url(r'^save/$', views.save, name="save"),


    
]

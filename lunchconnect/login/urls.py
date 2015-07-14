# Application login/views
from django.conf.urls import url

from . import views

urlpatterns = [
    # /login/
    url(r'^$', views.index, name='index'),
    # /login/1/
    url(r'^(?P<username_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /login/5/match/
    url(r'^(?P<username_id>[0-9]+)/match/$', views.match, name='match'),
    # ex: /login/5/signup/
    url(r'^(?P<username_id>[0-9]+)/signup/$', views.signup, name='signup'),
]

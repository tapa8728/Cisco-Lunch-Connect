from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Username, Password

# Create your views here.
def index(request):
    latest_username_list = Username.objects.order_by('-pub_date')[:5]
    template = loader.get_template('login/index.html')
    context = RequestContext(request, {
    	'latest_username_list': latest_username_list,
    	})
    #output = ', '.join([p.username_text for p in latest_username_list])
    #return HttpResponse(output)
    return HttpResponse(template.render(context))

def detail(request, username_id):
    return HttpResponse("Your are looking at the username with id %s." % username_id)

def match(request, username_id):
    response = "you are looking at the match for %s."
    return HttpResponse(response % username_id)

def signup(request, username_id):
    response = "Lets learn how connect pages with template %s."
    return HttpResponse(response % username_id)

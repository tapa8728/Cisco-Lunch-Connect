from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User

# Create your views here.
def index(request):
    latest_username_list = Username.objects.order_by('-pub_date')[:5]
    template = loader.get_template('login/index.html')
    context = {'latest_username_list': latest_username_list }
    return render(request, 'login/index.html', context)


# Render the sign up page
def signup(request):
    return render(request, 'login/signup.html')

# To save to DB
def save(request):
    print "now we will try to save"
    in_username = request.POST['inputUsername']
    in_firstname = request.POST['inputFirstName']
    in_lastname = request.POST['inputLastName']
    in_password = request.POST['inputPassword']
    in_designation = request.POST['inputDesignation']
    in_businessunit = request.POST['inputBU']
    #check for uniqueness before adding
    all_objects = User.objects.all()
    for obj in all_objects:
        if in_username == obj.username:
            print "Username already exists", in_username
            return render(request, 'login/login_alreadyexists.html')
            break           
        
    #Query to save to DB
    new_obj = User(username=in_username, firstname=in_firstname, password=in_password, lastname=in_lastname, designation=in_designation, businessunit=in_businessunit)
    new_obj.save()  #to save to DB
    return render(request, 'login/profile.html', {'user': new_obj})

# Render Login page
def login(request):
	return render(request, 'login/login.html')

# on click of submit button the u/p combo should go to database and check if it exists or not ????
# you will get the username from login.html
def submitform(request):
    if request.method == 'POST':
        input_username = request.POST['inputUsername']
        input_password = request.POST['inputPassword']
        #print input_username, "input_username"
        #print input_password, "input_password"
        all_objects = User.objects.all()
        count = User.objects.count()
        print "count is" , count
        for obj in all_objects:
            print input_username, obj.username
            print input_password, obj.password
            if input_username == obj.username:
                if input_password == obj.password:
                    print "----Match Found!!! YAY"
                    print "Designation is", obj.designation
                    if obj.designation == 'intern':
                        return render(request, 'login/profile_interns.html', {'user': obj})
                    else:
                        return render(request, 'login/profile_ciscoemployees.html', {'user': obj})
                    break           
            else:
                print "---Match Not Found"
        return render(request, 'login/login_incorrect.html')
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User, Appointment

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
        all_objects = User.objects.all()       #pull all user objects
        count = User.objects.count()
        print "count is :" , count
        for obj in all_objects:
            print input_username, obj.username
            print input_password, obj.password
            if input_username == obj.username:
                if input_password == obj.password:
                    print "----Match Found!!! YAY"
                    print "Designation is", obj.designation
                    if obj.designation == 'intern':
                        request.session['intern_username']=input_username
                        all_manager_appts = Appointment.objects.filter(booked=False)
                        intern_current_appts = Appointment.objects.filter(intern_username=input_username).filter(booked=True)
                        return render(request, 'login/profile_interns.html', {'user': obj, 'app_man_available':all_manager_appts, 'app_own_intern':intern_current_appts})
                    else:
                        request.session['manager_username']=input_username
                        all_app_objects_available = Appointment.objects.filter(manager_username=input_username).filter(booked=False)     #pull all available appointment objects
                        print "--all_app_objects_available", all_app_objects_available
                        all_app_objects_booked = Appointment.objects.filter(manager_username=input_username).filter(booked=True)     #pull all available appointment objects
                        return render(request, 'login/profile_ciscoemployees.html', {'user': obj, 'app_available': all_app_objects_available, 'app_booked': all_app_objects_booked})
                    break           
            else:
                print "---Match Not Found"
        return render(request, 'login/login_incorrect.html')

# To add a time slot for Manager
def addslot(request):
    if request.method == 'POST':
        print "Now we will try to add a new appointment"
        input_manager_username = request.session['manager_username']
        print "input_manager_username", input_manager_username
        input_inputDate = request.POST['inputDate']
        print "input_inputDate : ", input_inputDate
        input_inputStartTime = request.POST['inputStartTime']
        print "input_inputStartTime : ", input_inputStartTime
        input_inputEndTime = request.POST['inputEndTime']
        print "input_inputEndTime : ", input_inputEndTime
        input_inputLocation = request.POST['inputLocation']
        print "input_inputLocation : ", input_inputLocation
        input_inputAdditionalNotes = request.POST['inputAdditionalNotes']
        print "input_inputAdditionalNotes : ", input_inputAdditionalNotes
        #save to Appointment DB
        add_slot = Appointment(manager_username=input_manager_username, intern_username="_", location=input_inputLocation, additionalinfo=input_inputAdditionalNotes, booked=False, starttime=input_inputStartTime, endtime=input_inputEndTime, date=input_inputDate)
        add_slot.save()
        request.session['manager_username']=input_manager_username
        return render(request, 'login/index.html', {'appointment': add_slot})

#To book an appointment
def bookslot(request, appointment_id):
    app_to_book = get_object_or_404(Appointment, pk=appointment_id)
    print "Mananger :", app_to_book.manager_username
    #update it 
    k=request.session['intern_username']
    print "request.session['intern_username']", k
    Appointment.objects.filter(pk=appointment_id).update(intern_username=k)
    Appointment.objects.filter(pk=appointment_id).update(booked=True)
    print "Appointment is booked!"
    return render(request, 'login/index.html')
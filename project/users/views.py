from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import *
from job.models import *
from resume.models import *
from company.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_applicant(request):
    print('-----------------------------------------------------------------------')
    print(request)
    print('-----------------------------------------------------------------------')
    if request.method == 'POST':
        form = ResisterUserForm(request.POST)
        print('-----------------------------------------------------------------------')
        print(form.is_valid())
        print('-----------------------------------------------------------------------')
        print(form)
        print('-----------------------------------------------------------------------')
        print(request)
        print('-----------------------------------------------------------------------')
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.success(request, 'Account Created Successfully')
            return redirect('users:login_user')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('users:register_applicant')
    else:
        form = ResisterUserForm()
        context = {
            'form': form
        }
        return render(request, 'users/register_applicant.html', context)


def register_recruiter(request):
    if request.method == 'POST':
        form = ResisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            Resume.objects.create(user=var)
            messages.success(request, 'Account Created Successfully')
            return redirect('users:login_user')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('users:register_applicant')
    else:
        form = ResisterUserForm()
        context = {
            'form': form
        }
        return render(request, 'users/register_recruiter.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            user.is_online = True
            user.save()
            return redirect('dashboard:dashboard')

        else:
            messages.error(request,'something went wrong')
            return redirect('users:login_user')
    else:
        return render(request, 'users/login.html')

@login_required(login_url="users:login_user")
def logout_user(request):
    if request.user.is_authenticated:
        # Mark the user as offline (assuming you have an is_online field)
        request.user.is_online = False
        request.user.save()
        # Logout the user
        logout(request)
        # Add a logout message
        messages.info(request, 'Logged out successfully')
    # Redirect to the login page
    return redirect('users:login_user')

@login_required(login_url="users:login_user")
def myprofile(request):
    user = User.objects.get(id=request.user.id)
    print("_________________________________________________________")
    print(user)
    print("_________________________________________________________")
    context = {
        'user' :user
    }
    return render(request,'users/profile.html',context)
def elseProfile(request,pk):
    userdetails = User.objects.get(id=pk)
    jobs = Job.objects.filter(user = userdetails)
    
    print("_________________________________________________________")
    # print(myjobs)
    print("_________________________________________________________")
    context = {
        'userdetails' :userdetails,
        'jobs' :jobs
    }
    return render(request,'users/others_profile.html',context)

# def update_profile(request, pk):
#     user = User.objects.get(pk)
#     if  request.method=='POST':


def create_report(request,pk):
    user = User.objects.get(id=pk)
    repported_id = user  # Assuming you're passing the repported user's ID in the POST request
    if request.method == 'POST':
        message = request.POST.get('message')
        repporter = request.user  # Assuming the current user is the repporter
        print('_______________________________')
        print(user)
        print('_______________________________')

        # Check if the user has already reported the repported user
        count_reports = Repport.objects.filter(reported=repported_id).count()
        
        print(count_reports)
        
        if count_reports >= 10:
            repported_user = User.objects.get(id=pk)
            repported_user.is_active = False
            repported_user.save()

        # if existing_report:
        #     # If there's an existing report, just update the message and increment the counter
        #     existing_report.message = message
        #     existing_report.increment_counter()
        #     existing_report.save()
        # else:
            # If there's no existing report, create a new one
        repported = User.objects.get(pk=repported_id.id)  # Assuming User is your user model
        new_report = Repport.objects.create(reported_by=repporter, reported=repported, message=message)
        new_report.save()
        new_report.increment_counter()
        

        return redirect(f'users:elseProfile', pk )  # Redirect to a success page after reporting

    # If request method is GET, render the form for reporting
    return render(request, 'users/report_form.html')  # Assuming you have a template for the report form

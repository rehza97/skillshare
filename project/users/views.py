from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import *
from resume.models import *
from company.models import *

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

            return redirect('dashboard:dashboard')

        else:
            messages.error(request,'something went wrong')
            return redirect('users:login_user')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('users:login_user')

def myprofile(request,pk):
    user = User.objects.get(id=request.user.id)
    print("_________________________________________________________")
    print(user)
    print("_________________________________________________________")
    context = {
        'user' :user
    }
    return render(request,'users/profile.html',context)
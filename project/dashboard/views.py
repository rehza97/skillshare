from django.shortcuts import render , redirect
from django.urls import reverse
from job.models import Job, Category
from dashboard.form import ContactForm

from .filter import *
# Create your views here.
# def proxy(request):
#     if request.user.is_applicant:
#         return redirect('applicant_dashboard')
#     elif request.user.is_recruiter:
#         return redirect('recruiter_dashboard')
#     else:
#         return redirect('login_user')
        
# def applicant_dashboard(request):
#     return render(request , 'dashboard/applicant_dashboard.html')
        
# def recruiter_dashboard(request):
#     return render(request , 'dashboard/recruiter_dashboard.html')

def dashboard(request):
    jobs = Job.objects.all()
    myFilter = JobFilter(request.GET, queryset=jobs)
    categories = Category.objects.all()[:8]
    jobs = jobs[:4]
    rec_jobs = None  # Define rec_jobs here
    
    if request.user.is_authenticated:
        user = request.user
        rec_jobs = Job.objects.filter(user=user)
        
    jobs_counts = jobs.count()
    
    if request.GET:
        jobs = myFilter.qs
        # Get the current URL
        current_url = request.build_absolute_uri()
        # Find the index of the query string
        query_index = current_url.find('?')
        # If query parameters exist
        if query_index != -1:
            # Extract the query string
            query_string = current_url[query_index:]
            # Build the redirect URL
            redirect_url = reverse('dashboard:find_job') + query_string
            # Redirect to the URL
            return redirect(redirect_url)
    
    context = {
        "jobs": jobs,
        "jobs_counts": jobs_counts,
        "categories": categories,
        "rec_jobs": rec_jobs,
        "myFilter": myFilter,
    }
    return render(request, 'dashboard/dashboard.html', context)

def joblisting(request):
    myFilter = JobFilter()
    jobs = Job.objects.filter(is_available=True)
    myFilter = JobFilter(request.GET, queryset=jobs)
    jobs = myFilter.qs
    
    categories = Category.objects.all()
    jobs_counts = jobs.count()
    
    
    
    context = {
        "jobs" : jobs,
        "jobs_counts" : jobs_counts,   
        "categories" : categories,   
        "myFilter" : myFilter,   
    }
    return render(request , 'dashboard/job_listing.html',context)

def categories(request):
    categories = Category.objects.all()
    
    context = {
        "categories" : categories,
    }
    return render(request , 'dashboard/categories.html' , context)


def about(request):
    
    return render(request , 'dashboard/about.html' )

def contactUs(request):
    form = ContactForm()
    
    if request.method == 'POST' :
        if not request.user.is_authenticated:
            return redirect('users:login_user')  # Create a new form instance for GET requests or unauthenticated users
            
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.user = request.user  # Assign the current user to the user field
            contact_instance.save()
            # Optionally, you can redirect to a success page or display a success message
            return render(request, 'dashboard/contact.html')
        # If the form is not valid, render the form again with errors

    # Render the contact form template with the form context
    context = {
        "form": form,
    }
    return render(request, 'dashboard/contact.html', context)
    
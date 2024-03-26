from django.shortcuts import render , redirect
from job.models import Job, Category
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
    categories = Category.objects.all()[:8]
    jobs = Job.objects.filter(is_available=True)[:4]
    user = request.user
    rec_jobs = Job.objects.filter(user=user)
    jobs_counts = jobs.count()
    print(user)
    context = {
        "jobs" : jobs,
        "jobs_counts" : jobs_counts,
        "categories" : categories,
        "rec_jobs" : rec_jobs,
        
    }
    return render(request , 'dashboard/dashboard.html',context)

def joblisting(request):
    jobs = Job.objects.filter(is_available=True)
    jobs_counts = jobs.count()
    context = {
        "jobs" : jobs,
        "jobs_counts" : jobs_counts,   
    }
    return render(request , 'dashboard/job_listing.html',context)


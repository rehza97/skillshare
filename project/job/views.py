from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Job , ReviewRating
from .form import JobFormCreation , JobFormUpdate , CateFeed , ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="users:login_user")
def create_Job(request):
    if request.method == 'POST':
        form= JobFormCreation(request.POST,request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request,"Job is successfully posted!")
            # return redirect('job-detail',id=job.id)
            return redirect('dashboard:dashboard')
        else : 
            messages.warning(request,"please check the data u wrote something went wrong!")
    else:
        form = JobFormCreation()
        context = {
            'form' : form
        }
        return render(request , 'job/create_job.html',context)
@login_required(login_url="users:login_user")
def update_Job(request,pk):
    job_id = Job.objects.get(id=pk)
    if request.method == 'POST':
        form= JobFormUpdate(request.POST,request.FILES , instance=job_id )
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request,"Job details is successfully updated!")
            # return redirect('job-detail',id=job.id)
            return redirect('dashboard:dashboard')
        else : 
            messages.warning(request,"please check the data u wrote something went wrong!")
    else:
        form = JobFormUpdate(instance=job_id)
        context = {
            'form' : form
        }
        return render(request , 'job/update_job.html',context)
    
def job_details(request , pk):
    job = Job.objects.get(id = pk)
    comments = ReviewRating.objects.filter(job=job)
    print('____________________________________________________')
    print(comments)
    print('____________________________________________________')
    context = {
        'job' : job,
        'comments' : comments
    }
    return render(request , "job/job_details.html",context)
@login_required(login_url="users:login_user")
def FeedBack(request):
    if request.method=='POST':
        feedback=CateFeed(request.POST)
        if feedback.is_valid():
            feedback.save(comit=False)
            feedback.user= request.user
            feedback.save()
            messages.info(request,'Your request was sent succesafully')
        else:
            messages.warning(request,'something wrong happend please try again.')

# def review(request, pk):
#     url = request.META.get('HTTP_REFERER')
#     print('____________________________________')
#     print(pk)
#     if request.method == 'POST':
#         print("i'm inside  post method")

#         print("i'm inside  exception now")
#         form = ReviewForm(request.POST)
#         print(form.is_valid())
#         print('____________________________________')
#         if form.is_valid():
#                 data = ReviewRating()
#                 job_instance = Job.objects.get(id=pk)
#                 data.titre = request.POST.get('title') 
#                 data.review =request.POST.get('review')
#                 data.rating = request.POST.get('rating')
#                 data.ip = request.META.get('REMOTE_ADDR')
#                 data.job = job_instance
#                 data.user = request.user
#                 data.save()
#                 messages.success(request , 'Thank you, your comments have been sent successfully')
#                 return redirect(url)
#         else:
#                 messages.warning(request , 'something wen wrong')
#                 return redirect(url)
#     else:
#         return redirect(f'job_details/{pk}')
@login_required(login_url="users:login_user")
def review(request, pk):
    url = request.META.get('HTTP_REFERER')
    job_instance = get_object_or_404(Job, pk=pk)  # Get the job instance or return a 404 if not found
    
    if request.method == 'POST':
        title =  request.POST.get( "title" )
        rating =  request.POST.get( "rating" )
        review =  request.POST.get( "review" )
        print('__________________________________________________')
        print(rating)
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.rating = rating
            data.titre = title
            data.review = review
            data.job = job_instance
            data.ip = request.META.get('REMOTE_ADDR')
            if request.user.is_authenticated:
                data.user = request.user
                data.save()
                messages.success(request, 'Thank you, your comments have been sent successfully')
                return redirect(url)
            else:
                messages.warning(request, 'You need to be logged in to leave a review.')
        else:
            messages.warning(request, 'Something went wrong with the review submission.')
    return redirect(url or 'home')  # Redirect to the referring page or a default page if no referring page is found


@login_required(login_url="users:login_user")
def delete_job(requst , pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect('dashboard:dashboard')
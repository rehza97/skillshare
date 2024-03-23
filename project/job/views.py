from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Job , ReviewRating
from .form import JobFormCreation , JobFormUpdate , CateFeed , ReviewForm
# Create your views here.


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

    context = {
        'job' : job
    }
    return render(request , "job/job_details.html",context)

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

def review(request, pk):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        
            print("i'm inside  exception now")
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                job_instance = Job.objects.get(id=pk)
                data.titre = request.POST.get('title') 
                data.review =request.POST.get('review')
                data.rating = request.POST.get('rating')
                data.ip = request.META.get('REMOTE_ADDR')
                data.job = job_instance
                data.user = request.user
                data.save()
                messages.success(request , 'Thank you, your comments have been sent successfully')
                return redirect(url)
            else:
                messages.warning(request , 'something wen wrong')
                return redirect(url)
    else:
        return redirect(f'job_details/{pk}')
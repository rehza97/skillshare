from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from users.models import *
from .form import *
# Create your views here.
@login_required(login_url="users:login")
def update_company(request):
    company = Company.objects.get(user=request.user)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            request.user.has_company = True
            request.user.save()
            messages.success(request, "Your Company has been updated successfully. You can now start posting jobs.")
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Please correct the data you entered.')
    else:
        form = CompanyForm(instance=company)
    
    context = {'form': form}
    return render(request, 'company/update_company.html', context)


# view company detials
@login_required(login_url="users:login")
def  company_details(request,pk):
    company = Company.objects.get(id=pk)
    context={'company':company}
    return render(request,'company/view_company_details.html',context)
    
        
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Repport
class ResisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','phone','wilaya','baladia','email','password1','password2','address','job_title']


class ReportForm(forms.ModelForm):
    class Meta:
       model = Repport
       fields = ['message',]
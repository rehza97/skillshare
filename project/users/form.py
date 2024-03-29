from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Repport
class ResisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email','password1','password2']


class ReportForm(forms.ModelForm):
    class Meta:
       model = Repport
       fields = ['message',]
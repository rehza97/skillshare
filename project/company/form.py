from django import forms
from .models import Company




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        # exclude = ('user',)
        fields = ['name','city', 'state','est_date']

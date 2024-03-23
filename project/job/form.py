from django import forms
from .models import Job , CateFeed , ReviewRating
class JobFormCreation(forms.ModelForm):
    class Meta:
        model = Job
        fields=['title','location', 'description','price','is_available','category']
        
class JobFormUpdate(forms.ModelForm):
    class Meta:
        model = Job
        fields=['title','location', 'description','price','is_available','category']
        
class categoryFeedBackForm(forms.ModelForm):
    class Meta:
        model = CateFeed
        fields=['msg']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        exclude = ['titre','review','rating']
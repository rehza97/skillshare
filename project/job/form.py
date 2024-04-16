from django import forms
from .models import Job , CateFeed , ReviewRating
class JobFormCreation(forms.ModelForm):
    class Meta:
        model = Job
        fields=['title','Wilaya','banner','image1','image2','image3','image4', 'description','price','is_available','category']
        
class JobFormUpdate(forms.ModelForm):
    class Meta:
        model = Job
    fields=['title','Wilaya','banner','image1','image2','image3','image4', 'description','price','is_available','category']        
class categoryFeedBackForm(forms.ModelForm):
    class Meta:
        model = CateFeed
        fields=['msg']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        exclude = ['titre','review','rating']
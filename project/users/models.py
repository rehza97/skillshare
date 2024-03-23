from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20 , blank = True ,null = True)
    # profile_pic = 
    wilaya = models.CharField(max_length=20, blank = True ,null = True)
    address = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=20, blank = True ,null = True)

    # rating = 
    # signals = 
    is_recruiter= models.BooleanField(default =False)
    is_applicant= models.BooleanField(default =False)
    has_resume = models.BooleanField(default =False)
    has_company = models.BooleanField(default =False)
    
    
from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank = True ,null = True)
    last_name = models.CharField(max_length=50, blank = True ,null = True)
    phone = models.CharField(max_length=20 , blank = True ,null = True)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='media/profile/' ,blank=True, null=True )
    wilaya = models.CharField(max_length=20, blank = True ,null = True)
    baladia = models.CharField(max_length=20, blank = True ,null = True)
    address = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=20, blank = True ,null = True)
    

    # rating = 
    # signals = 
    is_online = models.BooleanField(default=False)
    is_recruiter= models.BooleanField(default =False)
    is_applicant= models.BooleanField(default =False)
    has_resume = models.BooleanField(default =False)
    has_company = models.BooleanField(default =False)
    
class Repport(models.Model):
    reported_by = models.ForeignKey(User, related_name='reported_by', on_delete=models.CASCADE)
    reported = models.ForeignKey(User, related_name='reported', on_delete=models.CASCADE)
    message = models.TextField()
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.reported_by} reported {self.reported}'
    
    def increment_counter(self):
        self.counter += 1
        self.save()



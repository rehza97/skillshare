from django.db import models
from users.models import *
# Create your models here.
class Resume(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100 , null=True , blank = True)
    username = models.CharField(max_length=100, null=True , blank = True)
    location = models.CharField(max_length=100, null=True , blank = True)
    job_title = models.CharField(max_length=100, null=True , blank = True)
    # gender = models.CharField(max_length=10)
    # birthday = models.DateField()
    # phone = models.CharField(max_length=20)
        
    def __str__(self) -> str:
        return self.username
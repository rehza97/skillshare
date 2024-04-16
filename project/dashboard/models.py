from django.db import models
from users.models import User
# Create your models here.

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self) -> str:
        return self.text +' by '+self.user.username
from django.db import models
from job.models import ReviewRating
from users.models import User
# Create your models here.

class ChatMessage(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='sent_messages',  on_delete=models.DO_NOTHING , blank = True , null = True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.DO_NOTHING, blank = True , null = True)
    seen = models.BooleanField(default=False , blank = True , null = True)
    
    def __str__(self) -> str:
        return self.body
    
    
class Contact(models.Model):
    sender = models.ForeignKey(User, related_name='my_account',  on_delete=models.DO_NOTHING , blank = True , null = True)
    receiver = models.ForeignKey(User, related_name='his_account', on_delete=models.DO_NOTHING, blank = True , null = True)
    
    def __str__(self) -> str:
        return f' sender {self.sender.username} / reciever : {self.receiver.username}'
    
class notification(models.Model):
    message = models.ForeignKey(ChatMessage ,on_delete = models.CASCADE)
    comment = models.ForeignKey(ReviewRating,on_delete = models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return  f'{self.message} or {self.comment}' 
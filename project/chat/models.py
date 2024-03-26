from django.db import models
from users.models import User
# Create your models here.

class ChatMessage(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.DO_NOTHING , blank = True , null = True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.DO_NOTHING, blank = True , null = True)
    seen = models.BooleanField(default=False , blank = True , null = True)
    
    def __str__(self) -> str:
        return self.body
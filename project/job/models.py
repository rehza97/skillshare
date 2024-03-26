from django.db import models

# Create your models here.
class Category(models.Model):
    banner =  models.ImageField(upload_to='category/banners/' , blank=True , null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
from users.models import User
class Job(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # banner =  models.ImageField(upload_to='post/banners/')
    description = models.TextField()
    category = models.ForeignKey(Category , on_delete=models.DO_NOTHING,blank=True , null = True )
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    # image1 = models.ImageField(upload_to='post/')
    # image2 = models.ImageField(upload_to='post/')
    # image3 = models.ImageField(upload_to='post/')
    # image4 = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class CateFeed(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    msg = models.TextField()

class ReviewRating(models.Model):
    job = models.ForeignKey(Job ,on_delete=models.CASCADE,blank=True , null = True)
    user = models.ForeignKey(User ,on_delete=models.CASCADE,blank=True , null = True)
    titre = models.CharField(max_length = 100,blank=True , null = True)
    review = models.TextField(blank=True , null = True)
    rating = models.FloatField(blank=True , null = True)
    ip = models.CharField(max_length=50,blank=True , null = True)
    state = models.BooleanField(default = True,blank=True , null = True)
    created_at =models.DateTimeField(auto_now_add=True,blank=True , null = True)
    
    def __str__(self):
        return self.titre
     
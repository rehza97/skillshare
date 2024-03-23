from django.contrib import admin
from .models import Job , Category , CateFeed , ReviewRating
# Register your models here.
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(ReviewRating)
admin.site.register(CateFeed)
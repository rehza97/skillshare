
from django.urls import path
from .views import *
app_name ='dashboard'
urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('categories/',categories, name='categories'),
    path('find_job/',joblisting, name='find_job'),
    path('about/',about, name='about'),
    path('contectUs/',contactUs, name='contectUs'),

]

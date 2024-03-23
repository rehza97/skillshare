
from django.urls import path
from .views import *
app_name ='company'
urlpatterns = [
path('create/',update_company, name='update_company'),
path('company/<str:pk>',company_details, name='company_details'),
]

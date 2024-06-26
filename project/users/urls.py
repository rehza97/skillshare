
from django.urls import path
from .views import *
app_name ='users'
urlpatterns = [
    path('applicant/regester/',register_applicant,name='register_applicant'),
    path('recruiter/regester/',register_recruiter,name='register_recruiter'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('myprofile/',myprofile,name='myprofile'),
    path('profile/<int:pk>',elseProfile,name='elseProfile'),
    path('report/<int:pk>',create_report,name='create_report'),
]

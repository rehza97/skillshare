
from django.urls import path
from .views import *
app_name ='job'
urlpatterns = [
path('createjob/', create_Job, name='create_job'),
path('updatejob/<int:pk>', update_Job, name='update_job'),
path('details/<int:pk>', job_details, name='job_details'),
path('review/<int:pk>', review, name='review'),
path('delete_job/<int:pk>', delete_job, name='delete_job'),
]

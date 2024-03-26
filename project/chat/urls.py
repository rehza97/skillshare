
from django.urls import path
from .views import *
app_name ='chat'
urlpatterns = [
path('<int:pk>',chat , name='chat'),
path('sentMsg/<int:pk>',sentMsg , name='sentMsg'),
path('recvMsg/<int:pk>',recvMsg , name='recvMsg')

]

from django.conf.urls import url
from django.urls import path
from . import views           # This line is new!
urlpatterns = [
    path('register', views.index),
    path('login', views.new),
    path('users/new', views.create),
    path('users', views.show),
    
] 



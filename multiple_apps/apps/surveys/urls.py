from django.conf.urls import url
from django.urls import path
from . import views           # This line is new!
urlpatterns = [
    path('surveys', views.index),
    path('surveys/new', views.new),
    
    # url(r'^$', views.index),
    # url(r'/new', views.new)  
] 



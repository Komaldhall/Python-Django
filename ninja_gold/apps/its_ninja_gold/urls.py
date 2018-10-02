from django.conf.urls import url
from django.urls import path
from . import views           # This line is new!
urlpatterns = [
    path('', views.index),
    path('process_money', views.process),
    path('clear', views.clear),
    
] 
from django.conf.urls import url
from django.urls import path
from . import views           # This line is new!
urlpatterns = [
    path('', views.index),
    path('add_word', views.add_word),
    path('clear', views.clear),
] 
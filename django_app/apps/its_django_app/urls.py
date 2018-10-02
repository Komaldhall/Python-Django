from django.conf.urls import url
from django.urls import path
from . import views           # This line is new!
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<str:number>', views.show),
    path('<str:number>/edit', views.edit),
    path('<str:number>/delete', views.destroy)
    # url(r'^$', views.index),
    # url(r'/new', views.new)  
] 



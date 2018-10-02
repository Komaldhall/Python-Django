from django.conf.urls import url
from django.urls import path
from . import views           # This line is new!
urlpatterns = [
    path('', views.index),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<str:number>', views.show),
    path('blogs/<str:number>/edit', views.edit),
    path('blogs/<str:number>/delete', views.destroy)
    # url(r'^$', views.index),
    # url(r'/new', views.new)  
] 



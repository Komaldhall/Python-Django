from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    path('users', views.index),
    path('users/new', views.add),
    path('users/<int:user_id>/destroy', views.delete),
    path('users/<int:user_id>/edit', views.edit),
    path('users/<int:user_id>',views.show),
    
]
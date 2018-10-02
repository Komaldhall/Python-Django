from django.urls import path
from . import views 
urlpatterns = [
    path('amadon', views.index),
    path('amadon/buy',views.buy),
    path('amadon/show',views.show),
    

  
]
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('destroy/<int:course_id>',views.remove),
    path('delete/<int:course_id>', views.delete),
   
]
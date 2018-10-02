from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('destroy/<int:course_id>',views.remove),
    path('comment/<int:course_id>',views.comment),
    path('delete/<int:course_id>', views.delete),
   
]
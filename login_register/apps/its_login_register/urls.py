from django.urls import path
from . import views 
urlpatterns = [
    path('', views.register),
    path('login', views.login),
    path('success', views.success),
    # path('register', views.register),
    # path('login', views.login),
    # path('logout', views.logout),
    # path('user/<int:user_id>', views.show)
]

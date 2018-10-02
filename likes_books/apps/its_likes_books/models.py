from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Books(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(default="description", max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader=models.ForeignKey(Users, related_name="uploaded_books", on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(Users, related_name="liked_books") 



# class Books(models.Model):
#     name=models.CharField(max_length=255)
#     desc=models.TextField(default="description", max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     uploaded_by_id=models.ForeignKey(Users, related_name="books")

# class Users(models.Model):
#     first_name=models.CharField(max_length=255)
#     last_name=models.CharField(max_length=255)
#     email=models.CharField(max_length=255)
#     books = models.ManyToManyField(Books, related_name="users") 
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True) 
    


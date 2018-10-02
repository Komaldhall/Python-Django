from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Desc(models.Model):
    course=models.OneToOneField(Course, related_name="my_desc", on_delete=models.CASCADE,primary_key=True)
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    courses=models.ForeignKey(Course, related_name="my_comments",on_delete=models.CASCADE, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



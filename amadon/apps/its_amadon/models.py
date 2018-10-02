from django.db import models

class Item(models.Model):
    content=models.CharField(max_length=100)
    price=models.IntegerField()
    value=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Stuff(models.Model):
    scontent=models.CharField(max_length=100)
    sprice=models.IntegerField()
    quantity=models.IntegerField()
    charge=models.CharField(max_length=3)



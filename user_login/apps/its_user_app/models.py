from __future__ import unicode_literals
from django.db import models
# from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def validate_email(email_address):
    if not EMAIL_REGEX.match(email_address):
        raise ValidationError({"Email not valid!!"})

def length(first_name):
    if len(first_name)<0:
        raise ValidationError({"Please provide first name!!"})

def length_l(last_name):
    if len(last_name)<0:
        raise ValidationError({"Please provide last name!!"})

class Users(models.Model):
    first_name=models.CharField(max_length=255, validators=[length])
    last_name=models.CharField(max_length=255, validators=[length_l])
    email_address=models.CharField(max_length=255,validators=[validate_email])
    #email_address=models.CharField(validators=[validate_email])
    age=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
      


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
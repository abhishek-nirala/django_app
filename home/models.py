from django.db import models
# from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    desc = models.TextField()
    date = models.DateField()
    
# name_validator = RegexValidator(r'^[a-zA-Z\s]*$', 'Enter a valid name (letters and spaces only).')
# special_char_validator = RegexValidator(r'^[a-zA-Z0-9@]*$', 'Only alphanumeric characters and @ are allowed.')

# class User(models.Model):
#     first_name = models.CharField(max_length=20, validators=[name_validator])
#     last_name = models.CharField(max_length=20, validators=[name_validator])
#     username = models.CharField(max_length=20, validators=[special_char_validator])
#     email  = models.EmailField(max_length=254)


def __str__(self):
    return self.name 
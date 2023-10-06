from django.db import models
from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
"""
username 
password
surname
lastname
"""
class User_password(models.Model):

    username = models.CharField(max_length=10,primary_key=True)
    password = models.CharField(max_length=5)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    row = models.CharField(max_length=10)
    last_login = models.DateTimeField(null=True, blank=True)
    def __str__(self) -> str:
        return f'{self.surname} {self.lastname}'


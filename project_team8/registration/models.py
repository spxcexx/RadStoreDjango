from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    number = models.IntegerField()
    email = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE)



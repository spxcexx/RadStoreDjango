from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_name = models.IntegerField()
    email = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE)



from django.db import models

# Create your models here.
class User_register(models.Model):

    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    category=models.CharField(max_length=10)

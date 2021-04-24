from django.db import models

# Create your models here.
class Register(models.Model):

    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    category=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    details=models.CharField(max_length=7)
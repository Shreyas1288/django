from django.db import models
# Create your models here.
class Student(models.Model):

    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)

#
# class Admin(models.Model):
#     institute_name=models.CharField(max_length=100)
#     admin_user=models.CharField(max_length=100)
#     admin_password=models.CharField(max_length=100)
#     admin_email = models.CharField(max_length=100)

class Status(models.Model):
    status=models.CharField(max_length=100)
    Dept=models.CharField(max_length=100)
    date=models.CharField(max_length=100)


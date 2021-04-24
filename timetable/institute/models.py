from django.db import models

# Create your models here.

class Login(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    branches_no = models.IntegerField()

class Institute_Details(models.Model):

    name=models.CharField(max_length=100)
    teachers_no=models.IntegerField()
    college_open=models.CharField(max_length=5)
    college_close=models.CharField(max_length=5)
    details=models.CharField(max_length=10,default="False")
    tdetails=models.CharField(max_length=10)
    c_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    slots=models.PositiveIntegerField(default=0)

class Branches(models.Model):
    b_name=models.CharField(max_length=100)
    c_id=models.ForeignKey(Login,on_delete=models.CASCADE)

class Teachers(models.Model):
    teacher_name=models.CharField(max_length=100)
    problem=models.CharField(max_length=100)
    classes=models.CharField(max_length=100)
    no_lectures=models.IntegerField(default=0)
    c_id=models.ForeignKey(Login,on_delete=models.CASCADE)
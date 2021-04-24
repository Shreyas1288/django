from django.db import models

# Create your models here.

class Doctor_register(models.Model):

    city=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    experiance=models.IntegerField()
    fees=models.IntegerField()
    speciality_name = models.CharField(max_length=200)
    clinic_name=models.CharField(max_length=500)
    details=models.CharField(max_length=5,default="false")
    doct_id=models.IntegerField(max_length=100)



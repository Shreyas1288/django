from django.db import models

# Create your models here.
class Appointment_register(models.Model):

    doct_name=models.CharField(max_length=100)
    doct_id=models.CharField(max_length=100)
    slot=models.CharField(max_length=100)
    patient_name=models.CharField(max_length=100)
    clinic_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)


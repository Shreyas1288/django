from django.db import models
from institute.models import Login
# Create your models here.

class Generate(models.Model):


    timetable=models.CharField(max_length=1000)
    c_id=models.ForeignKey(Login,on_delete=models.CASCADE)


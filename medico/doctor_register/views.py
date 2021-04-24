from django.shortcuts import render
from . models import Doctor_register
from django.http import HttpResponse
# Create your views here.

def profile(request,id):
    if request.method=="POST":
        obj=Doctor_register()
        city=request.POST["city"]
        obj.city=city
        degree=request.POST["degree"]
        obj.degree=degree
        speciality_name=request.POST["speciality"]
        obj.speciality_name=speciality_name
        obj.details="true"
        fees=request.POST["fees"]
        obj.fees=fees
        experiance=request.POST["experiance"]
        obj.experiance=experiance
        clinic_name=request.POST["clinic"]
        obj.clinic_name=clinic_name
        obj.doct_id=id
        obj.save()
        return(render(request,"index.html"))


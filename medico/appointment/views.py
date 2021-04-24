from django.shortcuts import render
from doctor_register.models import Doctor_register
from user_register.models import User_register
from .models import Appointment_register
from django.http import HttpResponse
# Create your views here.
def book_appointment(request):
    if(request.method=="POST"):
        obj = Doctor_register.objects.all()
        city = request.POST["city"]
        search = request.POST["speciality"]
        val=0
        list_var = []
        for i in obj:
            if ((i.speciality_name == search) and (i.city == city)):
                obj = User_register.objects.get(id=i.doct_id)
                val=val+1
                list_var.append([obj.name,i.speciality_name,i.experiance,i.fees,i.clinic_name,i.id])
        return (render(request, "book_appointment.html", {"list_var": list_var,"val":val,"city":city,"speciality":search}))

    elif(request.method=="GET"):
        obj = Doctor_register.objects.all()
        city = request.GET["city"]
        search =request.GET["speciality"]
        list_var = []
        val=0
        for i in obj:
            if ((i.speciality_name == search) and (i.city == city)):
                obj = User_register.objects.get(id=i.doct_id)
                val = val + 1
                list_var.append([obj.name, i.speciality_name, i.experiance, i.fees, i.clinic_name, i.id])
        return (render(request, "book_appointment.html", {"list_var": list_var, "val": val,"city":city,"speciality":search}))
    else:
        return("index.html")

def slot(request,id):
    obj=Appointment_register.objects.all()
    counter=0

    for i in obj:
        counter=counter+1
    counter=counter+1
    doct_id=(int)(id)
    return(render(request,"slot.html",{"counter":counter,"doct_id":doct_id}))

def success(request):
    if(request.method=="POST"):
        patient=request.POST["patient"]
        phone=request.POST["phone"]
        slot=request.POST["slot"]
        t_id=request.POST["t_id"]
        obj=Appointment_register.objects.all()
        obj3=Appointment_register()
        flag=0
        for i in obj:
            if((int)(i.id)==(int)(t_id)):
                return render(request,"error.html")

        id=request.POST["id"]
        obj1=User_register.objects.get(id=id)
        obj2=Doctor_register.objects.all()
        for i in obj2:
            if(i.doct_id==id):
                obj3.doct_name=obj1.name
                obj3.doct_id=id
                obj3.clinic_name=i.clinic_name
                obj3.patient_name=patient
                obj3.slot=slot
                obj3.phone=phone
                obj3.save()

                return(render(request,"success.html",{"doct_name":obj3.doct_name,"clinic_name":obj3.clinic_name,"patient_name":obj3.patient_name,"slot":obj3.slot,"phone":obj3.phone,"id":3}))
    else:
        return(render(request,"index.html"))



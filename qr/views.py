from django.shortcuts import render
import qrcode
from .models import Student,Status
from datetime import datetime
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect

def func(request):
    return(render(request,"qr/register.html"))


def func1(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        category=request.POST["category"]

#Check for duplicate Username and email

        a=Student()
        a.name=name
        a.email=email
        a.username=username
        a.password=password
        if category == "Register as Student":
            a.category="Student"
        else:
            a.category="Admin"

        a.save()
        return (HttpResponse("Data inserted successfully"))




    else:
        return(HttpResponse("Error"))

def func2(request):
    return (render(request,"qr/login.html"))

def func3(request):
    if request.method=="POST":
        username=request.POST["user"]
        password=request.POST["password"]
        content=Student.objects.all()
        for i in content:
            if((i.username==username) and (i.password==password) and (i.category=="Student")):

                a=Student.objects.get(id=i.id)
                context={"var_1":a}
                return(render(request,"qr/Student_View.html",context))

            elif(i.username==username and (i.password==password) and i.category=="Admin"):

                a = Student.objects.get(id=i.id)
                context = {"var_1": a}
                return (render(request, "qr/Admin_view.html", context))

        return(HttpResponse("Wrong Id or Password"))
    else:
        return (HttpResponse("Wrong id or Password"))

def func4(request):

    var_1=Student.objects.all()
    var_3=Status.objects.all()
    context={
        "var_1":var_1,
        "var_3":var_3


    }
    return (render(request,"qr/View1.html",context))

def func5(request,name,id):
    context={
        "name": name,
        "id": id
    }
    return(render(request,"qr/Status_view.html",context))

def func6(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        var_1=""
        var_2=""
        var_3=""
        pos=-1
        i=len(password)-1
        while(i>=0):
            if(password[i]=="@"):
                pos=i-1
                break
            else:
                var_1=var_1+password[i]
                i = i - 1
        i=pos
        while(i>=0):
            if(password[i]=="/"):
                pos=i-1
                break
            else:

                var_2= var_2+ password[i]
                i = i - 1
        i=pos
        while(i>=0):
            var_3=var_3+password[i]
            i = i - 1
        var_1=strrev(var_1)
        var_2=strrev(var_2)
        var_3=strrev(var_3)

        a=Student.objects.all()
        for i in a:
            if(i.username==username and i.password==var_3 and i.category=="Student"):
                try:
                    b=Status.objects.get(id=var_1)
                    return (render(request,"qr/qr_showstudent.html",{"var_1":b}))
                except Status.DoesNotExist:
                    return (Http404("File Does not Exists or Terminated" ))


            elif(i.username==username and i.password==var_3 and i.category=="Admin"):


                try:
                    b=Status.objects.get(id=var_1)
                    return (render(request,"qr/qr_showadmin.html",{"var_1":b}))

                except Status.DoesNotExist:
                    return (Http404("File Does not Exists or Terminated" ))


    else:
        return (HttpResponse("Error"))


def strrev(var_1):
    var_2=""
    i=len(var_1)-1
    while(i>=0):
        var_2=var_2+var_1[i]
        i=i-1
    return var_2

#Qr generate function

def func7(request):
    return(render(request,"qr/qrgenerate.html"))

def func8(request):
    if request.method=="POST":
        username=request.POST["username"]
        file_type=request.POST["file_type"]
        a=Status.objects.all()
        id=len(a)+1
        url="http://127.0.0.1:8000/mysite/status/"+str(username)+"/"+str(id)+"/"
        qr=qrcode.make(url)
        var="qr/static/qr/myqr"+str(id)+".png"
        qr.save(var)            #{% static '/qr/myqr1.png' %}
        var='/qr/myqr'+str(id)+'.png'
        a=Status()
        a.status="initial state"
        a.Dept="initial state"
        a.date="initial state"
        a.save()
        context={
            "var":var
        }
        return render(request,"qr/qr_view.html",context)
    else:
        return (HttpResponse("Error"))

def func9(request,id):
    return(render(request,"qr/edit_details.html",{"id":id}))

def func10(request):
    if request.method=="POST":
        var=request.POST["file_no"]
        a=Status.objects.get(id=var)
        a.status=request.POST["Status"]
        a.Dept=request.POST["Department"]
        a.date=datetime.now()
        a.save()
        return(HttpResponse("Details Updated Successfully"))
    else:
        return (HttpResponse("Error"))






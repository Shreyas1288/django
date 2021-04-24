from django.shortcuts import render
from .models import User_register
from django.http import HttpResponse
from doctor_register.models import Doctor_register
# Create your views here.

def home(request):
    if (request.session.has_key("active")==True):
        return render(request, "index.html",{"value":True,"username":request.session.get("username")})
    return(render(request,"index.html"))

def about(request):
    if (request.session.has_key("active")==True):
        return render(request, "about.html",{"value":True,"username":request.session.get("usernmae")})

    return render(request,"about.html")

def blog(request):
    if (request.session.has_key("active")==True):
        return render(request, "blog.html",{"value":True,"username":request.session.get("usernmae")})
    return(render(request,"blog.html"))

def blog_single(request):
    if (request.session.has_key("active")==True):
        return render(request, "blog-single.html",{"value":True,"username":request.session.get("usernmae")})
    return(render(request,"blog-single.html"))

def contact(request):
    if (request.session.has_key("active")==True):
        return render(request, "contact.html",{"value":True,"username":request.session.get("usernmae")})
    return(render(request,"contact.html"))

def department(request):
    if (request.session.has_key("active")==True):
        return render(request, "department.html",{"value":True,"username":request.session.get("usernmae")})
    return(render(request,"department.html"))

def register(request):
    if (request.session.has_key("active")==True):
        return render(request, "index.html",{"value":True,"username":request.session.get("usernmae")})
    return (render(request,"register.html"))

def login(request):
    if (request.session.has_key("active")==True):
        return render(request, "index.html",{"value":True,"username":request.session.get("usernmae")})
    return(render(request,"login.html"))

def register1(request):
    if (request.session.has_key("active")==True):
        return render(request, "index.html",{"value":True,"username":request.session.get("usernmae")})
    elif(request.method=="POST"):
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        number = request.POST["phone"]
        category=request.POST["category"]

        # Check Security

        obj = User_register()
        obj.name = name
        obj.email = email
        obj.password = password
        obj.phone = number
        obj.category=category
        obj.save()
        return (render(request,"index.html"))

    else:
        return(render(request,"register.html"))

def login1(request):
    if (request.session.has_key("active")==True):
        return render(request, "index.html",{"value":True,"username":request.session.get("usernmae")})
    elif request.method == "POST":
        obj=User_register.objects.all()
        obj1=Doctor_register.objects.all()
        flag=0
        email = request.POST["email"]
        password = request.POST["password"]
        for i in obj:
            if(i.email==email):
                if (i.password == password):
                    request.session["active"]=True
                    request.session["username"]=email
                    for j in obj1:
                        if((int)(j.doct_id) == (int)(i.id)):
                            flag = 1
                            print(flag)
                            return (render(request,"index.html"))
                    if(flag == 0 and i.category=="Doctor"):
                        return (render(request, "profile.html", {"id": i.id}))
                    else:
                        return (render(request, "index.html"))

    else:
        return (render(request,"login.html"))



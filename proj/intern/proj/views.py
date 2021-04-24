from django.shortcuts import render
from django.http import HttpResponse
from .models import Proj
from .serializers import ProjSerializer
from rest_framework import viewsets


class ProjViewSet(viewsets.ModelViewSet):
    queryset = Proj.objects.all()
    serializer_class = ProjSerializer


def index(request):
    return (render(request, "index.html"))


def register(request):
    if (request.method == "GET"):
        return (render(request, "register.html"))

    elif (request.method == "POST"):
        try:
            name = request.POST["name"]
            username = request.POST["username"]
            password = request.POST["password"]
            phone = request.POST["phone"]
            email = request.POST["email"]
        except KeyError:
            return (HttpResponse("Error 404"))

        if (name == "" or username == "" or password == "" or phone == "" or email == ""):
            return (HttpResponse("Error 404"))

        if (name.isalpha() == False):
            return (HttpResponse("Error 404"))

        if (phone.isdigit() == False or len(phone) != 10 or len(password) < 8):
            return (HttpResponse("Error 404"))

        obj = Proj()
        obj1 = Proj.objects.all()
        for i in obj1:
            if (i.username == username):
                return (HttpResponse("Error 404"))
        obj.name = name
        obj.password = password
        obj.email = email
        obj.username = username
        obj.phone = phone
        obj.save()
        return (render(request, "index.html"))
    else:
        return (HttpResponse("Error 404"))


def login(request):
    if (request.method == "GET"):
        return (render(request, "login.html"))
    elif (request.method == "POST"):
        try:
            username = request.POST["username"]
            password = request.POST["password"]
        except KeyError:
            return (HttpResponse("Error 404"))
        obj = Proj.objects.all()
        for i in obj:
            if (i.username == username and i.password == password):
                return (render(request, "success.html",
                               {"name": i.name, "username": i.username, "email": i.email,
                                "phone": i.phone}))
        return (HttpResponse("Error 404"))
    else:
        return (HttpResponse("Error 404"))

from django.shortcuts import render
from django.http import HttpResponse
from .serializers import PersonSerializer
from .models import Person
# Create your views here.
from rest_framework import viewsets
def func(request):
    return (render(request,"index.html"))
class PersonViewSet(viewsets.ModelViewSet):
    queryset =Person.objects.all().order_by("id")
    serializer_class = PersonSerializer

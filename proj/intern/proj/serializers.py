from rest_framework import serializers
from .models import Proj

class ProjSerializer(serializers.ModelSerializer):
    model=Proj
    fields=("username","email","phone","email")

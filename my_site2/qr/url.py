"""my_site2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("register/",views.func,name="func"),
    path("register1/",views.func1,name="func1"),
    path("login/",views.func2,name="func2"),
    path("login1/",views.func3,name="func3"),
    path("",views.func4,name="func4"),
    path("status/<name>/<id>/",views.func5,name="func5"),
    path("status1/",views.func6,name="func6"),
    path("qrgenerate/",views.func7,name="func7"),
    path("qrgenerate1/",views.func8,name="func8"),
    path("edit/<id>/",views.func9,name="func9"),
    path("edit1/",views.func10,name="func10"),
]

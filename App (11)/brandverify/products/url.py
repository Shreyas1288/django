"""brandverify URL Configuration

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

from django.urls import path
from . import views
urlpatterns = [
    path("",views.main,name="main"),
    path("register_cust/",views.register_cust,name="register_cust"),
    path("register_cust1/",views.register_cust1,name="register_cust1"),
    path("register_sales/",views.register_sales,name="register_sales"),
    path("register_sales1/",views.register_sales1,name="register_sales1"),
    path("login/",views.login,name="login"),
    path("login1/",views.login1,name="login1"),
]

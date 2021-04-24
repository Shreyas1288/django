from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
import math,random
from .models import Register
# Create your views here.
from twilio.rest import Client

def genrateOTP():
    digits = '0123456789'
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def main(request):
    return(render(request,"main.html"))

def register(request):
    return(render(request,"Register.html"))

def login(request):
    return(render(request,"Login.html"))

def login_user(request):
    if(request.method=="POST"):
        phone=request.POST["phone"]
        request.session["phone"]=phone
        phone="91"+str(phone)
        obj=Register.objects.all()
        flag=0
        for i in obj:
            if(i.phone==phone):
                otp=genrateOTP()
                request.session["id"]=i.id
                account_sid = 'AC6681de0b5775f2182b4b87261645f21e'
                auth_token = '65b4df8d32cbfd8d0500dfcb9cdd31c3'
                client = Client(account_sid, auth_token)
                request.session["otp"]=genrateOTP()
                otp=request.session.get("otp")
                message = client.messages.create(
                    to=phone,
                    from_="+14126853168",
                    body="Hello from Python!")
                flag=2
        if(flag=="0"):
            return (HttpResponse("Wrong Phone Number"))


        return (render(request,"login_otp.html"))

    else:
        return (HttpResponse("GET Requests are not allowed"))


def register_user(request):

    if(request.method=="POST"):
        email = request.POST['email']
        phone=request.POST["phone"]
        phone="+91"+str(phone)
        name=request.POST["name"]
        request.session["name"]=name
        request.session["phone"]=phone
        request.session["email"]=email
        request.session["otp1"]=genrateOTP()
        request.session["otp2"]=genrateOTP()
        subject = '@no reply otp for password reset'
        otp=request.session.get("otp1")
        message = 'please verify the otp to Register : ' +str(otp)
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        account_sid = 'AC6681de0b5775f2182b4b87261645f21e'
        auth_token = '65b4df8d32cbfd8d0500dfcb9cdd31c3'
        client = Client(account_sid, auth_token)
        otp=request.session.get("otp2")
        message = client.messages \
            .create(
            body="please verify the otp to Register :"+str(otp),
            from_='+14126853168',
            to=phone
        )
        return render(request,"verify.html")

    else:
        return (HttpResponse("GET Requests are not allowed"))

def verify_user(request):
    if(request.method=="POST"):
        otp3=request.POST["email"]
        otp4=request.POST["phone"]
        otp1=request.session.get("otp1")
        otp2=request.session.get("otp2")
        if(otp1==otp3 and otp2==otp4):
            obj=Register()
            name=request.session.get("name")
            obk.name=name.encode('base64','strict')
            email=request.session.get("email")
            obj.email=email.encode('base64',"strict")
            phone=request.session.get("phone")
            obj.phone=phone.encode('base64',"strict")
            obj.save()
            return(render(request,"register_success.html"))
        else:
            return (HttpResponse("Wrong OTP"))
    else:
        return (HttpResponse("GET Requests are not allowed"))

def login_verify(request):
    if(request.method=="POST"):
        if(request.session.get("otp")==request.POST["otp"]):
            id=request.session.get("id")
            obj=Register.object.get(id=id)
            name=obj.name.decode('base64',"strict")
            phone=obj.phone.decode("base64","strict")
            email=obj.email.decode("base64","strict")
            return (render(request,"Login_Success.html",{"name":name,"email":email,"phone":phone}))
        else:
            return (HttpResponse("Wrong OTP"))

    else:
        return (HttpResponse("GET Requests are not allowed"))
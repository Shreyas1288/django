from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Book
from django.shortcuts import render
# Create your views here.

def func(request):
    var=Book.objects.all()
    context={
        "var_name":var

    }
    return(render(request,"new_app1/index.html",context))

def func2(request,book_id):

    try:
        global book
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book not available")
    return(HttpResponse("<b>THe book details is "+str(book.name)+"</b>" ))

def func4(request):
    context={}
    return(render(request,"new_app1/form.html",context))

def func3(request):
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        c=Book()
        c.name=name
        c.age=age
        c.save()
        return(HttpResponse("Data added successfully"))
def func6(request):
    return(render(request,"new_app1/delete.html"))
def func5(request):
    id=None
    flag=0
    if request.method=="POST":
        username=request.POST["username"]
        var=Book.objects.all()
        for i in var:
            if i.name==username:
                id=i.id
                flag=1
        if flag==1:
            c=Book.objects.get(id=id)
            c.delete()
    return HttpResponse("Data deleted successfully")





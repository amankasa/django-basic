from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    tasks=Task.objects.all()
    contact={
       "tasks":tasks
    }
    return render(request,'index.html',contact)

def contact(request):
    return HttpResponse("Contact Please")
  

def about(request):
    # return HttpResponse("About Us")
    return render(request,'about.html')

def create(request):
    if request.method=="POST":
        return HttpResponse("this is a post request")
    # context={}
    # if request.method=="POST":
    #     name=request.POST.get("name")
    #     description=request.POST.get(name)
    #     if name is None and description is None:
    #         context={
    #             'error':"Both fields are required"
    #         }
    #     return HttpResponse()  
    return render(request,'create.html')


from django.shortcuts import render, HttpResponse,redirect
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
    # context={}
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        if not name and not description:
            context={
                "error":"Both fields are required"
            }
        else:
        # return HttpResponse(description)
            Task.objects.create(
                name=name,
                description=description
            )
            context={
                'success':"Task has been created"
            }
            return redirect('/')
        return render(request,'create.html',context)
    return render(request,'create.html')

def mark(request,pk):
    task=Task.objects.get(pk =pk)
    task.is_completed=True
    task.save()
    return redirect("/")


def delete(request,pk):
    Task.objects.get(pk=pk).delete()

    return redirect("/")

def edit(request,pk):
    task=Task.objects.get(pk=pk)
    context={
        'task':task
    }
    return render(request,'edit.html',context)

def update(request,pk):
    name=request.POST.get('name')
    description=request.POST.get('description')
    if not name and not description:
        context={
            "error":"Both fields are required"
        }
    task=Task.objects.get(pk=pk)
    task.name=name
    task.description=description
    task.save()
    return redirect("/")
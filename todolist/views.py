from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request,'index.html')

def contact(request):
    return HttpResponse("Contact Please")

def about(request):
    return HttpResponse("About Us")
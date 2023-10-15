from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request,'index.html')

def contact(request):
    # return HttpResponse("Contact Please")
    contact={
        "users":[
            {
                'name':'ram',
                'age':12,
            },
            {
        'name': 'sita',
        'age': 25,
    },
    {
        'name': 'lakshman',
        'age': 22,
    },
    
        ]
    }
    return render(request,'contact.html',contact)

def about(request):
    # return HttpResponse("About Us")
    return render(request,'about.html')

def create(request):
    if request.method=="POST":
        name=request.POST
        return HttpResponse()
    return render(request,'contact.html')


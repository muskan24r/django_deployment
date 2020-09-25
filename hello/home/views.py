from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    #return HttpResponse("hello muskan")
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')
    #return HttpResponse("hello about")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("hello services")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'your message have been submitted!')
    return render(request,'contact.html')
    #return HttpResponse("hello contact")

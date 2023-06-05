from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminapp.models import *
from django.contrib import auth
from . models import *

# Create your views here.
def index(request):
    data=Adddb.objects.all()
    return render(request,"index.html",{'data':data})
def register(request):
    return render(request,"register.html")

def getdata(request):
    if request.method=="POST":
        name=request.POST.get('name') 
        email=request.POST.get('email')
        phn=request.POST.get('phn')
        address=request.POST.get('address')
        password=request.POST.get('password')
        data=Registrationdb(name=name,email=email,phn=phn,address=address,password=password)
        data.save()
        return redirect("index")

def viewdata(request):
    data=Registrationdb.objects.all()

    return render(request,"viewdata.html",{'data':data})



def login(request):
    return render(request,"login.html")

def getlogin(request):
    if request.method=="POST":
        email=request.POST.get('email')     #input type's emails name
        password=request.POST.get('password')
        if Registrationdb.objects.filter(email=email,password=password).exists():   #first email is what in db
            return redirect('loginhome')
        else:
            return render(request,"login.html",{'msg':'invalid user credentials'})
    else:
        return render(request,"index")


def booking(request):
    data=Admindb.objects.all() #this is how dataabse elemets are accessed all objects
    return render(request,"booking.html",{'data':data})

def getbooking(request):
    if request.method=="POST":
        pname=request.POST.get('pname') 
        address=request.POST.get('address')
        phn=request.POST.get('phn')
        plants=request.POST.get('plants')
        data=Bookingdb(pname=pname,address=address,phn=phn,plants=plants)
        data.save()
        return redirect("loginhome")
    
def loginhome(request):
    return render(request,'loginhome.html')


def Logout(request):
    auth.logout(request)
    return redirect("index")

def edit(request,did):
    data= Registrationdb.objects.filter(id=did)
    return render(request,"edit.html",{'data':data})

def update(request,did):
    if request.method=="POST":
        name=request.POST.get('name') 
        email=request.POST.get('email')
        phn=request.POST.get('phn')
        address=request.POST.get('address')
        password=request.POST.get('password')

        Registrationdb.objects.filter(id=did).update(name=name,email=email,phn=phn,address=address,password=password)
        return redirect('viewdata')
    
def delete(request,did):
    Registrationdb.objects.filter(id=did).delete()
    return redirect('viewdata')

def addplant(request):
    return render(request,"addplant.html")

def getplant(request):
    if request.method=='POST':
        plant_image=request.FILES['plant_image']
        plantname=request.POST.get('plantname')
        description=request.POST.get('description')
        data=Adddb(plant_image=plant_image,plantname=plantname,description=description)
        data.save()
        return redirect("addplant")
    
def viewplant(request):
    data=Adddb.objects.all()
    return render(request,"viewplant.html",{'data':data})

def view(request,did):
    data=Adddb.objects.filter(id=did)
    return render(request,"view.html",{'data':data})

def viewbooking(request):
    data=Bookingdb.objects.all()
    return render(request,"viewbooking.html",{'data':data})
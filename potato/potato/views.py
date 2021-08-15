from django.shortcuts import render
from .models import *
# Create your views here.
def profile(request):
    return render(request,'profile.html')

def dishes(request):
    return render(request,'dishes.html')

def index(request):
    dest=Destination.objects.filter().all()
    data=[]
    for i in dest:
        print(i)
        x=dict(destinations= dict(name=i.name, description= i.description, image= i.image, offer= i.offers) )
        data.append(x)
    print(data)
    return render(request,'index.html', {'data': data})

def hotels(request, destination):
    city= Destination.objects.get(name=destination)
    hotels=Hotels.objects.filter(destination=city).all()
    data=[]
    for i in hotels:
        print(i)
        x=dict(hotels= dict(name=i.name, description=i.description, image= i.image, offer= i.offers, likes= i.likes))
        data.append(x)
    print(data)
    return render(request,'hotels.html', {'data':data})

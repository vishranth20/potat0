from django.shortcuts import *
from django.http import *
from django.contrib.auth import authenticate, login, logout
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

def logoutUser(request):
    logout(request)
    return redirect('/')

def loginPage(request):
    if request.method == 'POST':

        if 'submit' in request.POST:
            username =request.POST['username']
            password =request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse('Wrong username or password')
    else:
        return render(request, 'login.html')
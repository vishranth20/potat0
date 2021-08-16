from django.shortcuts import *
from django.http import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def profile(request):
    return render(request,'profile.html')

def dish(request, destination,hotel):
    city= Destination.objects.get(name=destination)
    hotels=Hotels.objects.get(name=hotel,destination=city)
    dishes = Dishes.objects.filter(hotel=hotels).all()
    data=[]
    for i in dishes:
        print(i)
        x=dict(city=city,hotel=hotels,dish= dict(name=i.name, likes=i.likes, offer= i.offer,description= i.description,image= i.image, price= i.price))
        data.append(x)
    print(data)
    return render(request,'food.html', {'data':data})

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
        x=dict(city=city,hotels= dict(name=i.name, description=i.description, image= i.image, offer= i.offers, likes= i.likes))
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

def register(request):
    form=registerform()
    if request.method == 'POST':
        print('1')
        form=registerform(request.POST)
        print(form)
        if form.is_valid():
            print('2')
            form.save()
            return redirect("/login")
        else:
            print('2no')
            print(form.errors)
            messages.info(request,str(form.errors))
            return redirect('/register')
    else:
        print('1no')
        context={'form':form}
        return render(request,'register.html',context)

            
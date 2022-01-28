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
        x=dict(city=city,hotel=hotels,dish= dict(id= i.id,name=i.name, likes=i.likes, offer= i.offer,description= i.description,image= i.image, price= i.price))
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
    print(destination)
    banner = []
    if destination == 'Chennai':
            banner = ['https://cdn.discordapp.com/attachments/782108008053604353/932225255622201415/4883007.png','https://cdn.discordapp.com/attachments/782108008053604353/932225365924020254/Basera-indian-Cuisine-In-Plano.png','https://cdn.discordapp.com/attachments/782108008053604353/932225493875429406/18f57eee6880cc86544dd4bba55fb9fb.png']
    elif destination == 'Delhi':
            banner = ["https://cdn.discordapp.com/attachments/782108008053604353/932225648070651934/GettyImages-579154550_1-73e0815d601b.png","https://cdn.discordapp.com/attachments/782108008053604353/932225781105582110/b75c88369e1763169d4a2a29a2d7587c.png","https://cdn.discordapp.com/attachments/782108008053604353/932226335621914655/1739009.jpg"]
    elif destination == 'Mumbai':
            banner = ["https://cdn.discordapp.com/attachments/782108008053604353/932226480434458684/df.png","https://cdn.discordapp.com/attachments/782108008053604353/932226614568300574/1316965.png","https://cdn.discordapp.com/attachments/782108008053604353/932226770361548831/maxresdefault.png"]
    hotels=Hotels.objects.filter(destination=city).all()
    hots = []
    for i in hotels:
        print(i)
        x=dict(name=i.name, description=i.description, image= i.image, offer= i.offers, likes= i.likes)
        hots .append(x)
    data={'cityname':city.name,'cityimg':banner,'hotels':hots}
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

def pay(request):
        return render(request,'pay.html')
        
def scam(request):
        return render(request,'scam.html')

def about(request):
    posts =[
        {
                'Name': 'Vishranth',  
                'Post': 'CEO',
                'School': 'Saraswathi vidyalaya',
                'Company': 'of POTATO food app'
        },
        {
                'Name': 'Pranesh',
                'Post': 'COO',
                'School': 'Saraswathi vidyalaya',
                'Company': 'of POTATO food app'
        },

        {
                'Name': 'Deepak',
                'Post': 'MANAGER',
                'School': 'Saraswathi vidyalaya',
                'Company': 'of POTATO food app'
        }
]
    return render(request,'about.html',{"posts":posts})

def addtocart(request,productid):
    if request.user.is_authenticated:
        if addToCart.objects.filter(user=request.user).exists():

            cart= addToCart.objects.get(user=request.user)
            products=Dishes.objects.get(id=productid)

            cart.product.add(products)
            return HttpResponse(status=204)
        else:
            product=Dishes.objects.get(id=productid)
            
            cart= addToCart.objects.create(user=request.user)
            cart.product.add(product)
            
            return render(request,"pay.html")

def addtocart_display(request):
    if request.method=="POST":
        return HttpResponse("POST")
    else:
        cart=addToCart.objects.get(user=request.user)
    add=[]
    for i in cart.product.all():
        print(i)

        usercart= {'Product_name':i.name, 'Product_id': i.id,'Product_price': i.price, 'Product_image': i.image}
        print(i)
        add.append(usercart)
    return render(request,"addtocart.html",{'data':add})
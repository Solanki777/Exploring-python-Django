from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login




# Create your views here.
def rec_show(request):
    if request.method=="POST":
        data=request.POST

        rec_image=request.FILES.get('recipe_image')
        rec_name=data.get('recipe_name')
        rec_dec=data.get('recipe_description')

        Receipe.objects.create(
            receipe_name=rec_name,
            receipe_description=rec_dec,
            receipe_image=rec_image
            )
        
        # redirect to page if you not right this when you refresh the project it will again add details to the database
        return redirect('recepy')
        
    queryset=Receipe.objects.all()
    search=request.GET.get('search')

    if search:
        queryset=queryset.filter(receipe_name=search)
        
    context={'receipes':queryset }


    return render(request,'rec.html',context)






# TO UPDATE 
def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)

    if request.method=="POST":

        queryset.receipe_description=request.POST.get('recipe_description')
        queryset.receipe_name=request.POST.get('recipe_name')

        if request.FILES.get('recipe_image'):
            queryset.receipe_image=request.FILES.get('recipe_image')
        
        queryset.save()
        return redirect('recepy')
    
    context={
        'receipe':queryset
    }
    return render(request,'rec_update.html',context)
        






# TO DELETE RECEIPE 
def delete_receipe(request,id):
    
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('recepy')



def login_page(request):

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            return render(request,'login.html',{'error': 'username not found'})
        
        # here we encrypted the password so we have to use authentication function from the auth 

        user = authenticate(username=username ,  password=password)

        if user==None:
            return render(request,'login.html',{'error': 'invalid credential'})
        
        # for successfull login we redirect user to main page but here we use the session to maintain the user login info using login function from the same directory as authentication 
        else:
            login(request,user)
            return redirect('/rec/')
        
    return render(request, 'login.html')


def register_page(request):

    if request.method== "POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')

        # if user name is already taken         
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error': 'Username already exists'})
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password

        )

        # to encrypt data 
        user.set_password(password)
        user.save()

        return redirect('/login/')

    
    return render(request,'register.html')



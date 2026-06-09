from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    people=[
        {"name" : "Mahesh" ,"Age":23},
        {"name" : "Montu" ,"Age":23},
        {"name" : "Harpal" ,"Age":22, "city":"botad"},
        {"name" : "Kuldip" ,"Age":22},
        {"name" : "Harsad" ,"Age":10}
    
    ]
    text="This is a Student details from the Khas village"

    likes=["Apple","Banana","Orange","Graps"]

    for p in people:
        print(p)
    return render(request,"index.html",context={
        'page': 'Djanog tutorial ', 
        'p':people,
        't':text,
        'fruit':likes
        })

def successpage(request):
    print("*"*10)
    return HttpResponse("<h1>this is successpage</h1>")

def about(request):

    # used show in url 
    context ={ 'page' : 'About'}

    return render(request,"about.html",context)

def contact(request):
    context = { 'page' : 'Contact'}
    return render(request,"contact.html",context)


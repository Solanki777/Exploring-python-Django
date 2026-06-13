from django.shortcuts import render,redirect
from .models import *

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
    context={'receipes':queryset }

    return render(request,'rec.html',context)

def delete_receipe(request,id):
    
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('recepy')



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



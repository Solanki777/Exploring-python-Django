from django.shortcuts import render
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



    return render(request,'rec.html')
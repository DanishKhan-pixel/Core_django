from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import*

# Create your views here.


def receipes(request):
   if request.method =="POST":
    data=request.POST
    
    name=data.get("name")
    description=data.get("description") 
    image=request.FILES.get("image")
   

    Receipe.objects.create(
      name=name,
      image=image,  
      description=description,
     

    )
    return redirect('/receips/')
    


   #  print(name)
   #  print(description)
   #  print(image)



   return render(request, "vege/receipe.html")






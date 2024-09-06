from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def receipes(request):
   if request.method =="POST":
    data=request.POST
    
    name=data.get("name")
    description=data.get("description") 
    image=request.FILES.get("image")

    print(name)
    print(description)
    print(image)
   return render(request, "vege/receipe.html")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def receipes(request):
   return render(request, "vege/receipe.html")

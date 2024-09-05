from django.urls import path
from . import views

urlpatterns = [
    path("receips/", views.receipes, name="receipes"), 
]

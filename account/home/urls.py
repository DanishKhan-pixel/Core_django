from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Correctly matches the root URL of the 'home' app
]

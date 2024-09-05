from django.db import models

# Create your models here.
class Receipe(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=600)
    image=models.ImageField(upload_to="Receipe")



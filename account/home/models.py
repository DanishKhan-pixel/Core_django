from django.db import models
# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_hire = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

class Car(models.Model):
    name=models.CharField(max_length=23)
    speed=models.IntegerField(default=30)
    def __str__(self):
        return f"{self.name} {self.speed}"




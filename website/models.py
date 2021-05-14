from django.db import models


# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    date=models.DateField()
    schedule=models.CharField(max_length=100)
    message=models.TextField()

class Reply(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100) 
    message=models.CharField(max_length=100)   
    
    
    
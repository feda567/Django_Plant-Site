from django.db import models

# Create your models here.

class Registrationdb(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phn=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=6)

class Bookingdb(models.Model):
    pname=models.CharField(max_length=20)
    address=models.TextField()
    phn=models.IntegerField()
    plants=models.CharField(max_length=30)

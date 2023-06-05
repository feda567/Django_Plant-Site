from django.db import models

# Create your models here.
class Admindb(models.Model):
    plantname=models.CharField(max_length=20)
    plantimage=models.ImageField(upload_to='image',default="null.jpg")

class Adddb(models.Model):
    plant_image=models.ImageField(upload_to='image',default='null')
    plantname=models.CharField(max_length=20)
    description=models.CharField(max_length=100)

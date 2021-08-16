from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import *
from django.utils.timezone import datetime

class Destination(models.Model):
    name=models.CharField(max_length=100, null=False)
    description=models.TextField()
    image=models.ImageField()
    offers=models.BooleanField()
    def __str__(self):
        return self.name 

class Hotels(models.Model):
    destination= models.ForeignKey(Destination,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, null=False)
    description=models.TextField()
    image=models.ImageField()
    likes=models.IntegerField()
    offers=models.BooleanField()
    def __str__(self):
        return self.name


class Dishes(models.Model):
    hotel=models.ManyToManyField(Hotels)
    name=models.CharField(max_length=100, null=False)
    image=models.ImageField()
    description=models.TextField()
    offer=models.BooleanField(default=False)
    likes=models.IntegerField()
    price=models.FloatField()
    def __str__(self):
        return self.name  
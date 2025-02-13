from django.db import models
from django.contrib.auth.models import AbstractUser


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    persons = models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    nm = models.CharField(max_length=100)
    em = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return self.nm



class Signup(models.Model):  # Change 'signup' to 'Signup'
    na = models.CharField(max_length=100)
    el = models.EmailField(unique=True)
    pas = models.CharField(max_length=255)  # Store hashed passwords

    def __str__(self):
        return self.na

class Signin(models.Model):
    us = models.CharField(max_length=100)
    pa = models.CharField(max_length=100, null=False)
     # Allow NULL values or remove it

    def __str__(self):
        return self.us

from django.db import models
#from django.contrib.auth.models import AbstractUser, Group, Permission


# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name; # Removed unnecessary semicolon

# Property Model

class Signup(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords!

    def __str__(self):
        return self.username

class Schedule(models.Model):
    nm = models.CharField(max_length=100)
    em = models.EmailField(max_length=100)
    da = models.DateField()
    ti = models.TimeField()

    def __str__(self):
        return self.nm

from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from testApp.models import Contact,Reservation,Signup,Signin

def index(request):
    return render(request, "testApp/index.html")

def about(request):
    return render(request, "testApp/about.html")

def contact(request):
    if request.method == "POST":
        nm = request.POST.get("nm")
        em = request.POST.get("em")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save data to database
        new_contact = Contact(nm=nm, em=em, subject=subject, message=message)
        new_contact.save()

        return HttpResponse("Thank you! Your message has been received.")  # Simple response

    return render(request, "testApp/contact.html")


def menu(request):
    return render(request, "testApp/menu.html")


def reservation(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        persons = request.POST.get("persons")

        reserve = Reservation(name=name, email=email, date=date, persons=persons)
        reserve.save()


    return render(request, "testApp/reservation.html")

def service(request):
    return render(request, "testApp/service.html")

def testimonial(request):
    return render(request, "testApp/testimonial.html")

def signup(request):
    if request.method == "POST":
        na = request.POST.get("na")
        el = request.POST.get("el")
        pas = request.POST.get("pas")


        user = Signup(na=na, el=el, pas=pas)
        user.save()

    return render(request, "testApp/signup.html")


def signin(request):
    if request.method == "POST":
        us= request.POST.get("us")
        pa= request.POST.get("pa")

        ue=Signin(us=us, pa=pa)
        ue.save()

    return render(request, "testApp/signin.html")

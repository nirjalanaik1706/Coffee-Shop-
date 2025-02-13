from django.shortcuts import render, redirect
from django.contrib import messages
from MyApp.models import Contact, Schedule,Signup

# Index View
def index(request):
    return render(request, "MyApp/index.html")

# Contact View
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save data to database
        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        new_contact.save()
    return render(request, "MyApp/contact.html")

# Property List View
def property(request):
    return render(request, 'MyApp/properties.html')

# Property Details View
def property_details(request):
    return render(request, "MyApp/property-details.html")


# Signup View
def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        en=Signup(email=email,username=username,password=password)
        en.save()

    return render(request, "MyApp/signup.html")

# Login View
def login(request):
    return render(request, "MyApp/login.html")

# Logout View
def logout(request):
    return redirect("/login/")

# Schedule a Visit View
def schedule(request):
    if request.method == "POST":
        nm = request.POST.get('nm')
        em = request.POST.get('em')
        da = request.POST.get('da')
        ti = request.POST.get('ti')

        sa=Schedule(nm=nm,em=em,da=da,ti=ti)
        sa.save()

    return render(request, "MyApp/schedule.html")

from django.contrib import admin
from django.urls import path
from testApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),  # 👈 Default route for homepage
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("menu/", views.menu, name="menu"),
    path("reservation/", views.reservation, name="reservation"),
    path("service/", views.service, name="service"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup")

]

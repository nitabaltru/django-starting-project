"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("admin/", admin.site.urls, name="admin"),
    # Bands
    path("bands/", views.band_list, name="band_list"),
    path("bands/<int:id>/", views.band_detail, name="band_detail"),
    path("bands/add/", views.band_create, name="band_create"),
    path("bands/<int:id>/change/", views.band_change, name="band_change"),
    path("bands/<int:id>/delete/", views.band_delete, name="band_delete"),
    # Listings
    path("listing/", views.listing_list, name="listing_list"),
    path("listing/<int:id>/", views.listing_detail, name="listing_detail"),
    path("listing/add/", views.listing_create, name="listing_create"),
    path("listing/<int:id>/change/", views.listing_change, name="listing_change"),
    path("listing/<int:id>/delete/", views.listing_delete, name="listing_delete"),
    # General
    path("about-us/", views.about, name="about"),
    path("contact-us/", views.contact, name="contact"),
    path("email-sent/", views.sent, name="email-sent"),
]

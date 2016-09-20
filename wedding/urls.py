"""wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main_view, name='main_view'),
    url(r'^wedding$', views.details_view, name='details_view'),
    url(r'^travel$', views.travel_view, name='travel_view'),
    url(r'^photos$', views.photo_view, name='photo_view'),
    url(r'^registry$', views.registry_view, name='registry_view'),
    url(r'^rsvp$', views.rsvp_view, name='rsvp_view'),
    url(r'^rsvpsubmit$', views.rsvp_post, name='rsvp_post')
]

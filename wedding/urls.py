
from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^topsecret/', include(admin.site.urls)),
    url(r'^$', views.main_view, name='main_view'),
    url(r'^wedding$', views.details_view, name='details_view'),
    url(r'^travel$', views.travel_view, name='travel_view'),
    url(r'^photos$', views.photo_view, name='photo_view'),
    url(r'^registry$', views.registry_view, name='registry_view'),
    url(r'^rsvp$', views.rsvp_view, name='rsvp_view'),
    url(r'^rsvp_thanks$', views.rsvp_success, name='rsvp_success'),
    url(r'^rsvpsubmit$', views.rsvp_post, name='rsvp_post')
]

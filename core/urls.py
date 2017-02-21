from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home_url'),
 	url(r'^support/', views.support, name='support_url'),
 	url(r'^contact/', views.contact, name='contact_url'),
 	url(r'^events/', views.events, name='events_url'),
]
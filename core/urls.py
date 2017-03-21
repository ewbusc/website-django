from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home_url'),
    url(r'^edit/$', views.edit_home, name='edit_home_url'),
    url(r'^support/', views.support, name='support_url'),
    url(r'^contact/', views.contact, name='contact_url'),
    url(r'^events/', views.events, name='events_url'),
    url(r'^projects$', views.projects, name='projects_url')
]

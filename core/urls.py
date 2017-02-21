from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home_url'),
    url(r'^projects$', views.projects, name='projects_url')
]

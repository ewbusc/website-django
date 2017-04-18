from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home_url'),
    url(r'^support/$', views.SupportView.as_view(), name='support_url'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact_url'),
    url(r'^events/$', views.EventsView.as_view(), name='events_url'),
    url(r'^projects/$', views.ProjectsView.as_view(), name='projects_url'),
    url(r'^edit/$', views.EditHomeView.as_view(), name='edit_home_url'),
    url(r'^edit/support/$', views.EditSupportView.as_view(), name='edit_support_url'),
    url(r'^edit/events/$', views.EditEventsView.as_view(), name='edit_events_url'),
    url(r'^edit/projects/$', views.EditProjectsView.as_view(), name='edit_projects_url')
]

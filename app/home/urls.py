from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ticket_data/', views.ticket_data, name='ticket-data'),
]
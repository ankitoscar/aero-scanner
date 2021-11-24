from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/busiest_month', views.busiest_month, name='busiest_month'),
    path('dashboard/price_analysis', views.price_analysis, name='price_analysis'),
    path('dashboard/on_time', views.on_time_performance, name='on_time'),
    path('dashboard/most_travelled', views.most_travelled, name="most_travelled"),
    path('dashboard/most_booked', views.most_booked, name='most_booked'),
]
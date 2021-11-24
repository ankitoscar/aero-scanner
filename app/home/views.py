from django.shortcuts import render
from django.http import JsonResponse
from .dashboard import Dashboard

d = Dashboard()

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html')

def busiest_month(request):
    data = d.busiest_month('BOM', '2017', 'ARRIVING')
    return JsonResponse(data, safe=False)

def price_analysis(request):
    data = d.price_analysis('BOM', 'DEL', '2021-11-23')
    return JsonResponse(data, safe=False)

def on_time_performance(request):
    data = d.on_time_performance('BOM', '2021-11-23')
    return JsonResponse(data, safe=False)

def most_travelled(request):
    data = d.most_travelled('BOM', '2017-12')
    return JsonResponse(data, safe=False)

def most_booked(request):
    data = d.most_booked('BOM', '2017-12')
    return JsonResponse(data, safe=False)

def dashboard(request):
    return render(request, 'home/dashboard.html')
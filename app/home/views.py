from django.shortcuts import render
from django.http import JsonResponse
from .dashboard import Dashboard

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html')

def ticket_data(request):
    d = Dashboard()
    data = d.busiest_month('BOM', '2017', 'ARRIVING')
    return JsonResponse(data, safe=False)


def dashboard(request):
    return render(request, 'home/dashboard.html')
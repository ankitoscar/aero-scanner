from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html')

def ticket_data(request):
    if request.method == 'POST':
        _to = request.POST['']

def dashboard(request):
    return render(request, 'home/dashboard.html')
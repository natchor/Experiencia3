from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'apps/home.html')

def somos(request):

    return render(request, 'apps/somos.html')

def galeria(request):

    return render(request, 'apps/galeria.html')

def Unetenos(request):

    return render(request, 'apps/Unetenos.html')
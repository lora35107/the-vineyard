from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')
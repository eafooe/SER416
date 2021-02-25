from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    logout(request)

def about(request):
    return render(request, 'about.html')

def calendar(request):
    return render(request, 'calendar.html')

def programs(request):
    return render(request, 'programs.html')

def contact(request):
    return render(request, 'contact.html')

def facilities(request):
    return render(request, 'facilities.html')

def donate(request):
    return render(request, 'donate.html')

def reservations(request):
    return render(request, 'reservations.html')


def profile(request):
    return render(request, 'profile.html')

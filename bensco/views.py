from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginPage(request):
    page = 'login'
    context = {'page': page}
    return render(request, 'bensco/login_registration.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    context = {}
    return render(request, 'bensco/login_registration.html', context)

def bensco(request):
    context = {}
    return render(request, 'bensco/bensco.html', context)

def drawerPage(request):
    context = {}
    return render(request, 'bensco/drawer.html', context)

def homePage(request):
    context = {}
    return render(request, 'bensco/home.html', context)

def tripsPage(request):
    context = {}
    return render(request, 'bensco/trips.html', context)

def trucksPage(request):
    context = {}
    return render(request, 'bensco/trucks.html', context)

def usersPage(request):
    context = {}
    return render(request, 'bensco/users.html', context)

def customersPage(request):
    context = {}
    return render(request, 'bensco/customers.html', context)

def reportsPage(request):
    context = {}
    return render(request, 'bensco/reports.html', context)
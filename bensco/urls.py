from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.bensco, name='bensco'),
    path('drawer/', views.drawerPage, name='drawer'),
    path('home/', views.homePage, name='home'),
    path('trips/', views.tripsPage, name='trips'),
    path('trucks/', views.trucksPage, name='trucks'),
    path('users/', views.usersPage, name='users'),
    path('customers/', views.customersPage, name='customers'),
    path('reports/', views.reportsPage, name='reports'),
]
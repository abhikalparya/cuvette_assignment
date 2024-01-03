from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is our homepage!")

def profile(request):
    return HttpResponse("This is our profile page!")

def login(request):
    return HttpResponse("This is our login page!")

def register(request):
    return HttpResponse("This is our registration page!")

def logout(request):
    return HttpResponse("This is our logout page!")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'loginauth/home.html')

def profile(request):
    return render(request, 'loginauth/profile.html')

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, 'Wrong password or username')
            return redirect('login')
        
    return render(request, 'loginauth/login_page.html')

def register_user(request):
    return render(request, 'loginauth/register_page.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')
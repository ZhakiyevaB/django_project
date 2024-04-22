
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse


def login(request): #controller 
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['userame']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
        else:
            form = UserLoginForm()

    context = {
        'title': 'Home - Login',
        'form': form,
    }
    return render(request,'users/login.html', context)

def registration(request): #controller 
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instanse
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - registration',
        'form': form
    }
    return render(request,'users/registration.html', context)

def profile(request): #controller 

    context = {
        'title': 'Home - profile',
        

    }
    return render(request,'users/profile.html', context)

def logout(request): #controller 
    auth.logout(request)
    return redirect(reverse('main:index'))

from email import message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib import auth
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

from django.contrib import messages


def login(request): #controller 
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['userame']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{user.username}, You are welcome")
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
            messages.success(request, f"{user.username}, You are succesfuly registratd in account")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - registration',
        'form': form
    }
    return render(request,'users/registration.html', context)

@login_required
def profile(request): #controller 
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instanse=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{user.username}, Profile succesfuly uploaded")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instanse=request.user)

    context = {
        'title': 'Home - profile',
        'form': form
    }
    return render(request,'users/profile.html', context)

def logout(request): #controller 
    messages.success(request, f"{request.user.username}, You logout of account")
    auth.logout(request)
    return redirect(reverse('main:index'))

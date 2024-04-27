from email import message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib import auth, messages
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def login(request): #controller 
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, You are in account")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
        else:
            form = UserLoginForm()

    context = {
        'title': 'Home - login',
        'form': form
    }
    return render(request,'users/login.html', context)

def registration(request): #controller 
    form = UserLoginForm()
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
    form = UserLoginForm()
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile succesfuly uploaded")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)


    context = {
        'title': 'Home - profile',
        'form': form
    }
    return render(request,'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request): #controller 
    messages.success(request, f"{request.user.username}, You logout of account")
    auth.logout(request)
    return redirect(reverse('main:index'))

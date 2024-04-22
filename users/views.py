
from django.http import HttpResponseRedirect
from django.shortcuts import render

from users.form import UserLoginForm


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
    context = {
        'title': 'Home - registration',
    }
    return render(request,'users/registration.html', context)

def profile(request): #controller 

    context = {
        'title': 'Home - profile',
        

    }
    return render(request,'users/profile.html', context)

def logout(request): #controller 

    context = {
        'title': 'Home - logout',
        

    }
    return render(request,'', context)

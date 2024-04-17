
from django.shortcuts import render


def login(request): #controller 

    context = {
        'title': 'Home - Login',
        

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

from django.http import HttpResponse
from django.shortcuts import render

def index(request): #controller 
    context = {
        'title': 'PharmPlus - Main',
        'content': " Pharmacy store PharmPlus",

    }
    return render(request,'main/index.html', context)

def about(request): #controller 
    context = {
        'title': 'PharmPlus - About Us',
        'content': " we are ",
        'text_on_page': 'Lorrwm lorwjfhduivd',

    }
    return render(request,'main/about.html', context)
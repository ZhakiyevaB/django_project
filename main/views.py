from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request): #controller 

    categories = Categories.objects.all()

    context = {
        'title': 'Home - main',
        'content': " Store Home ",
        'categories': categories

    }
    return render(request,'main/index.html', context)

def about(request): #controller 
    context = {
        'title': 'Home - About Us',
        'content': " About us ",
        'text_on_page': 'Lorrwm lorwjfhduivd',

    }
    return render(request,'main/about.html', context)
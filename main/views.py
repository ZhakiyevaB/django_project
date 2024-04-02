from django.http import HttpResponse
from django.shortcuts import render

def index(request): #controller 
    context = {
        'title': 'Home',
        'content': 'Main page of Pharmacy - PharmaPlus',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False,
    }
    return render(request,'main/index.html', context)

def about(request): #controller 
    return HttpResponse('About Page')
from django.core.paginator import Paginator
from unicodedata import category
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.template import context

from goods.models import Products
from goods.utils import q_search

from django.contrib.postgres.fields import JSONField

#from rest_framework import generics
#from .models import Products
#from .serializers import ProductSerializer

##from django.shortcuts import render, redirect, get_object_or_404
#from .forms import ProductForm
#from .models import Products

#from django.forms import ProductForm  # Assuming you have a form defined for Product model


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug =='all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug)) 
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by  != "default":
        goods = goods.order_by(order_by)
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = { 
        'title': 'Home - Catalog',
        'goods': current_page,
        'slug_url': category_slug
        }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug ):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)


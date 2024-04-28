from urllib import response
from django.shortcuts import redirect, render
from carts.templatetags.carts_tags import user_carts
from carts.utils import get_user_carts
from goods.models import Products
from unicodedata import category
from carts.models import Cart
from users.models import User
from django.template.loader import render_to_string

def cart_add(request, product_slug ):

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity +=1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])
        

def cart_change(request, cart_id):
    quantity = request.POST.get("quantity")
    cart = Cart.objects.get(id=cart_id)

    if quantity is not None:
        cart.quantity = quantity
        cart.save()


    return redirect(request.META['HTTP_REFERER'])

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)

    cart.delete()



    return redirect(request.META['HTTP_REFERER'])
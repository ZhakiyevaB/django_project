from atexit import register
from django import template
from carts.models import Cart
from carts.utils import get_user_carts
from users.models import User

register = template.Library()

@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
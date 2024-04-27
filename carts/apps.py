from django.apps import AppConfig
from traitlets import default

class CartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'
    verbose_name = 'Корзины' 


from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

app_name ='users'

urlpatterns = [
    path('login', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    #path('users-cart/', views.users_cart, name='users_cart'),
    path('logout/', views.logout, name='logout'),
]

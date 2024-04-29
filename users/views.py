from email import message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib import auth, messages
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from users.models import User
from rest_framework.response import Response

from django.urls import reverse

def login(request): #controller 
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, You are in account")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
        else:
            form = UserLoginForm()

    context = {
        'title': 'Home - login',
        'form': form
    }
    return render(request,'users/login.html', context)

def registration(request): #controller 
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, You are succesfuly registratd in account")
            return HttpResponseRedirect(reverse('main:index'))
        else:
            form = UserRegistrationForm()

    context = {
        'title': 'Home - registration',
        'form': form
    }
    return render(request,'users/registration.html', context)

@login_required
def profile(request): #controller 
    form = UserLoginForm()
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile succesfuly uploaded")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)


    context = {
        'title': 'Home - profile',
        'form': form
    }
    return render(request,'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request): #controller 
    messages.success(request, f"{request.user.username}, You logout of account")
    auth.logout(request)
    return redirect(reverse('main:index'))
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Userz
from .serializers import UserzSerializer


class UserzAPIView(APIView):
    def get(self, request):
        w = Userz.objects.all()
        return Response({'posts': UserzSerializer(w, many=True).data})

    def post(self, request):
        serializer = UserzSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Userz.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = UserzSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        # здесь код для удаления записи с переданным pk

        return Response({"post": "delete post " + str(pk)})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Userz
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import UserzSerializer


class UserzAPIList(generics.ListCreateAPIView):
    queryset = Userz.objects.all()
    serializer_class = UserzSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class UserzAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Userz.objects.all()
    serializer_class = UserzSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class UserzAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Userz.objects.all()
    serializer_class = UserzSerializer
    permission_classes = (IsAdminOrReadOnly, )

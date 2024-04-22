from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()
    
  #  username = forms.CharField(
  #      label = 'Name',
  #      widget=forms.TextInput(attrs={"autofocus": True,
  #                             'class': 'form-control',
  #                             'placeholder': 'Text username'}))
  #  password = forms.CharField(
  #     label = 'password',
  #      widget=forms.PasswordInput(attrs={"autocomplete": "current-possword",
  #                                  'class': 'form-control',
  #                                  'placeholder': 'Text username'}))


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
        first_name = forms.CharField(required=False)
        last_name = forms.CharField()
        username = forms.CharField()
        email = forms.CharField()
        password1 = forms.CharField()
        password2 = forms.CharField()


#    first_name = forms.CharField(
#        widget=forms.TextInput(
#            attrs={
#                  'class': 'form-control',
#                  'placeholder': 'text your firstname'}))
#   last_name = forms.CharField(
#       widget=forms.PasswordInput(
#            attrs={
                  'class': 'form-control',
                  'placeholder': 'text your lastname'}))
#    username = forms.CharField(
#        widget=forms.TextInput(
#            attrs={
#                  'class': 'form-control',
#                  'placeholder': 'Text username'}))
#    email = forms.CharField(
#        widget=forms.TextInput(
#            attrs={
#                  'class': 'form-control',
#                  'placeholder': 'Text email'})) 

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )
        first_name = forms.forms.CharField()
        last_name = forms.forms.CharField()
        username = forms.forms.CharField()
        email = forms.forms.CharField()


#    image = forms.ImageField(
#        widget = forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
#    )
#    first_name = forms.CharField(
#        widget=forms.TextInput(
#            attrs={
#                  'class': 'form-control',
#                  'placeholder': 'text your firstname'}))
#    last_name = forms.CharField(
#        widget=forms.PasswordInput(
#            attrs={
#                  'class': 'form-control',
#                  'placeholder': 'text your lastname'}))
#    username = forms.CharField(
#        widget=forms.TextInput(
#            attrs={
#                  'class': 'form-control',
#                  'placeholder': 'Text username'}))
#    email = forms.CharField(
#        widget=forms.TextInput(
#            attrs={
#                  'class': 'form-control',
#                  'placeholder': 'Text email'}))
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    
    #username = forms.CharField(
       # label = 'Name',
      #  widget=forms.TextInput(attrs={"autofocus": True,
       #                        'class': 'form-control',
       #                        'placeholder': 'Text username'}))
  # password = forms.CharField(
    #   label = 'password',
     #   widget=forms.PasswordInput(attrs={"autocomplete": "current-possword",
     #                               'class': 'form-control',
     #                               'placeholder': 'Text username'}))

    class Meta:
        model = User
        fields = ['username', 'password']
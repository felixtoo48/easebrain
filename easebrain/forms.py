from django import forms
from .models import *
from django.db import models
from django.contrib.auth.forms import UserCreationForm
# from django.forms import widgets

"""
#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
"""


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

"""
class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
                            required=True)
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={'id': 'floatingPassword', 'class': 'form-control mb-3'}),
                            required=True)

    class Meta:
        model=User
        fields=['username','password']
"""

class UserProfile(forms.ModelForm):
    """ users profile input form """
    name = models.CharField(null=True, blank=True, max_length=200)
    phoneNumber = models.CharField(null=True, blank=True, max_length=15)
    userLogo = models.ImageField(null=True, blank=True, upload_to='logos', default='')
    title = models.CharField(choices=CATEGORY, blank=True, max_length=100)
    addressLine1 = models.CharField(null=True, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        model=UserProfile
        fields=['name', 'phoneNumber', 'userLogo', 'title', 'addressLine1', 'postalCode']

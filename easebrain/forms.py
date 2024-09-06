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
    CATEGORY = [
            ('Mr', 'Mr'),
            ('Mrs', 'Mrs'),
            ('Dr', 'Dr'),
            ]
    GENDER = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ]
    STATUS = [
            ('Single', 'Single'),
            ('Married', 'Married'),
            ('Divorced', 'Divorced'),
            ('Widowed', 'Widowed'),
            ('Separated', 'Separated'),
            ]
    title = models.CharField(choices=CATEGORY, blank=True, max_length=100)
    name = models.CharField(null=True, blank=True, max_length=200)
    gender = models.CharField(choices=GENDER, blank=True, max_length=50)
    phoneNumber = models.CharField(null=True, blank=True, max_length=15)
    userLogo = models.ImageField(null=True, blank=True, upload_to='logos', default='')
    addressLine1 = models.CharField(null=True, blank=True, max_length=100)
    birthDate = models.DateTimeField(null=True, blank=True)
    next_of_kin = models.CharField(null=True, blank=True, max_length=200)
    maritalStatus = models.CharField(choices=STATUS, blank=True, max_length=100)
    date_of_enrollment = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    class Meta:
        model=UserProfile
        fields=['title', 'name', 'gender', 'phoneNumber', 'userLogo', 'addressLine1', 'birthDate', 'next_of_kin', 'maritalStatus', 'date_of_enrollment', 'summary']

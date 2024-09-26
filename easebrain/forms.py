from django import forms
from .models import *
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.contrib.auth import get_user_model

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column

User = get_user_model()


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email already exists.')
        return email


class UserProfileForm(forms.ModelForm):
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

    # user = forms.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = forms.ChoiceField(choices=CATEGORY, required=True, label='Title',)
    name = forms.CharField(required=True, label='Enter Full Name',)
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Select your Gender',)
    phoneNumber = forms.CharField(required=True, label='Enter your Phone Number',)
    userLogo = forms.ImageField(required=True, label='Add profile picture',)
    addressLine1 = forms.CharField(required=True, label='Enter your address',)
    birthDate = forms.DateField(required=True, label='Date of Birth', widget=DateInput(attrs={'class': 'form-control'}),)
    next_of_kin = forms.CharField(required=True, label='Next of Kin',)
    maritalStatus = forms.ChoiceField(choices=STATUS, required=True, label='Select your status',)
    date_of_enrollment = forms.DateTimeField(required=True, label='Date of Enrollment',)
    summary = forms.CharField(required=True, label='Add short summary',)

    class Meta:
        model = UserProfile
        fields = ['user', 'title', 'name', 'gender', 'phoneNumber', 'userLogo', 'addressLine1', 'birthDate', 'next_of_kin', 'maritalStatus', 'date_of_enrollment', 'summary']

        widgets = {
                'birthDate': forms.DateInput(attrs={'type': 'date'}),
                'summary': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            }

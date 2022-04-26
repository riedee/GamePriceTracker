"""
A module to handle the user creation form and structure
Inputs: UserCreationForm
"""


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """Create form for registration"""
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=30, required=True, help_text='')

    class Meta:
        """Define user and fields for registration"""
        model = User
        fields = ('username', 'first_name', 'last_name',
                    'email', 'password1', 'password2', )
                    
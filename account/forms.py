from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class DoctorRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        #label = {''}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            
        }


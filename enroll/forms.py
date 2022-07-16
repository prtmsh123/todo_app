from dataclasses import field, fields
from tkinter import Widget
from unicodedata import name
from django import forms
from django.core import validators
from .models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        Widgets = {
            
            
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.EmailInput(attrs={'class':"form-control"}),
            'password': forms.PasswordInput(render_value=True,attrs={'class':"form-control"}),


        }
 
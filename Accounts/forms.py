from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):
    terms=forms.BooleanField()
    class Meta:
        model = Customer
        fields = ["username","email","phone_number", "password", "password2","pincode","terms"]
        exclude = ()
        widgets = {
      'password': forms.PasswordInput()
         }

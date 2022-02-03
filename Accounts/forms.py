from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):
  class Meta:
        model = Customer
        fields = ("username", "phone_number", "email", "password", "pincode")
        exclude = ()


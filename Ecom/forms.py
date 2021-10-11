from django import forms
from .models import Requestbook


class RequestForm():
  class Meta:
        model = Requestbook
        feilds = "__all__"
        exclude = ()

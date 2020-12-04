from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.forms import BSModalModelForm

class EmailModelForm(BSModalModelForm):
    class Meta:
        model = User
        fields = ['email']
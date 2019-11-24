
from django import forms

from .models import User,Store

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'username']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email','username','password']

class StoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields=['name','address','city']
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Ваш логин')
    password1 = forms.CharField(label='Введите пароль', strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
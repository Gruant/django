from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.EmailField(label='Ваш логин', max_length=100, widget=forms.EmailInput(
                                    attrs={'class': 'form-control first-field',
                                           'placeholder': 'Email',
                                           }))
    password1 = forms.CharField(label='Введите пароль', strip=False, widget=forms.PasswordInput(
                                   attrs={'class': 'form-control last-field',
                                          'placeholder': 'Пароль',
                                          }))
    password2 = forms.CharField(label='Повторите пароль',  widget=forms.PasswordInput(
                                   attrs={'class': 'form-control last-field',
                                          'placeholder': 'Пароль',
                                          }))


class ReviewForm(forms.Form):
    name = forms.CharField(label='Имя', required=False, max_length=150,
                           widget=forms.TextInput(attrs={'placeholder': 'Представьтесь', 'class': 'form-control'}))
    description = forms.CharField(label='Ваш отзыв',
                                  widget=forms.Textarea({'placeholder': 'Содержание', 'class': 'form-control'}),
                                  required=True)
    mark = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)],
                             widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), required=True)




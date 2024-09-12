from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": 'text',
                'placeholder': 'Введите логин'
            }
        ),
        required=False,
    )

    password = forms.EmailField(
        widget=forms.PasswordInput(
            attrs={
                 "autocomplete": 'current-password',
                'placeholder': 'Введите пароль'
            }
        ),
        required=False,
    )

    error_messages = {
        "invalid_login": ('Введите логин и пароль правильно')
    }

    def clean_password(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Введите логин', code='invalid')
        if not User.objects.get(username=username):
            raise forms.ValidationError('Такого пользователя не существует', code='invalid')
        return username
    
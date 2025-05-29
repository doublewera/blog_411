from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {}
        for fieldname in fields:
            help_texts[fieldname] = None
        labels = {
            "username": "Ваш логин",
            "password": "Пароль"
        }

    
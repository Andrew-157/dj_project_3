from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm,\
    UserChangeForm as BaseUserChangeForm


class UserCreationForm(BaseUserCreationForm):
    email = forms.EmailField(required=True,
                             help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password1', 'password2', 'image'
        ]


class UserChangeForm(BaseUserChangeForm):
    email = forms.EmailField(required=True,
                             help_text='Required. Enter a valid email address.')
    password = None

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'image'
        ]

from django import forms

from demo.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, min_length=6)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20, min_length=8)
    email = forms.CharField(widget=forms.EmailInput, max_length=255)

    class Meta(object):
        model = User
        fields = ('username', 'password', 'email')

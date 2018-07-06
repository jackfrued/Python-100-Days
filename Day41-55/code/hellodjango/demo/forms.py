from django import forms

from demo.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, min_length=6, max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    email = forms.CharField(widget=forms.EmailInput, max_length=255)

    class Meta(object):
        model = User
        fields = ('username', 'password', 'email')

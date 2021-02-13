from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class LoginForm(forms.ModelForm):
    class Meta:
        models = User
        fields = ['username', 'password']
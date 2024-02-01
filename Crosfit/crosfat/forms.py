
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password']
class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password')
        help_texts = {
            'password': None,  # To usunie tekst pomocy
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = None
        # Usuń informacje o algorytmie hashowania
        if 'instance' in kwargs:
            self.fields['password'].required = False
            self.fields['password'].widget = forms.PasswordInput()
            self.fields['password'].help_text = 'Wprowadź nowe hasło lub pozostaw puste, aby zachować obecne.'
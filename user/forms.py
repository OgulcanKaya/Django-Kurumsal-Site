from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, Select, FileInput, EmailInput

from Home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)
        widgets = {
            'username': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Email Adress'}),
            'first_name': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Last Name'}),
        }

CITY = [

    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
    ('Eskişehir', 'Eskişehir'),
    ('Mersin', 'Mersin'),
    ('Karabük', 'Karabük'),
]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'adress', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Phone'}),
            'adress': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Adress'}),
            'city': Select(attrs={'class=form-control valid': 'input', 'placeholder': 'City'}, choices=CITY),
            'country': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'Image'}),
        }

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class ChefCreatorForm(UserCreationForm):
    role = forms.CharField(max_length=50)
    speciality_food = forms.CharField(max_length=50)

    class Meta:
        model = get_user_model()
        fields = ['username', 'role', 'speciality_food']

class ConnectChef(forms.Form):
    username = forms.CharField(max_length=63,label='Nom utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

    

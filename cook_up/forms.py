from django import forms
from cook_up.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['creator', 'steps', 'ingredients']


class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['creator', 'steps', 'ingredients']
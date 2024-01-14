from django.shortcuts import render, get_object_or_404, redirect
from cook_up.models import Recipe
from cook_up.forms import RecipeForm, RecipeUpdateForm

from django.contrib.auth.decorators import login_required



@login_required
def create_recipe(request):
    recipe_form = RecipeForm()
    message = ''
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = Recipe()
            recipe.creator = recipe_form.cleaned_data['creator']
            recipe.steps = recipe_form.cleaned_data['steps']
            recipe.ingredients = recipe_form['ingredients']
            recipe.save()
            return redirect('get-recipes')
        else:
            message = 'verify entered data !'
    else:
        message = 'method is not post !'
    return render(request, 'cook_up/cook.html', {'recipe_form':recipe_form, 'message':message})


@login_required
def get_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'cook_up/recipes.html', {'recipes':recipes})


@login_required
def update_recipe(request, id):
    recipe_instance = get_object_or_404(Recipe, id=id)
    recipe_form = RecipeUpdateForm(instance=recipe_instance)
    message = ''
    if request.method == "POST":
        recipe_form = RecipeUpdateForm(request.POST, instance=recipe_instance)
        if recipe_form.is_valid():
            recipe_form.save()
            message = 'recipe modified succefully !'
        else:
            message ='form is not valid! please check your data'
    return render(request, 'cook_up/update_recipe.html', {'message':message, 'recipe_form':recipe_form})

@login_required
def delete_recipe(request, id):
    recipe_instance = get_object_or_404(Recipe, id=id)
    recipe_instance.delete()
    return redirect('get-recipes')

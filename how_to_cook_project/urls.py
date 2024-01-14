"""
URL configuration for how_to_cook_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication_app_management.views import signup_user, login_to_app, home, logout_user
from cook_up.views import create_recipe, get_recipes, update_recipe, delete_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup_user/', signup_user, name='signup-user'),
    path('login_to_app/', login_to_app, name='login-app'),
    path(' home/',  home, name='home'),
    path('logout_user/', logout_user, name='logout-user'),
    path('create_recipe/', create_recipe, name='create-recipe'),
    path('get_recipes/', get_recipes, name='get-recipes'),
    path('update_recipe/<int:id>/change', update_recipe, name='update-recipe'),
    path('delete_recipe/<int:id>/delete', delete_recipe, name='delete-recipe'),
]

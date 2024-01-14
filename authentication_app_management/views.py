from django.shortcuts import render, redirect
from authentication_app_management.forms import ChefCreatorForm, ConnectChef
from authentication_app_management.models import ChefCuisineModel
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from authentication_app_management import forms



def signup_user(request):
    form = ChefCreatorForm()
    message = ''
    if request.method == "POST":
        form = ChefCreatorForm(request.POST)
        if form.is_valid():
            user = ChefCuisineModel()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.role = form.cleaned_data['role']
            user.speciality_food = form.cleaned_data['speciality_food']
            user.save()
            message = "user created succefully !"
        else:
            form = ChefCreatorForm(request.POST)
            message = "form is not valid !"
    return render(request, 'authentication_app_management/signup.html', context={'message':message, 'form':form})



def login_to_app(request):
    form = ConnectChef()
    message = ''
    username =''
    password = ''
    if request.method == "POST":
        form = ConnectChef(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'check username and password !'
        
    return render(request, 'authentication_app_management/login_page.html', context={'message':message,'form':form, 'username':username, 'password':password})



@login_required
def home(request):
    message = 'welcome to home !'
    return render(request, 'authentication_app_management/home.html', {'message':message})


def logout_user(request):
    logout(request)
    return redirect('login-app')







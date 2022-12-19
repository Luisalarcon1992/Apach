from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})      

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_date['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user) 
            return redirect(to='blog')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
        }
    return render(request, 'registration/register.html', context)




from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from blog.forms import ContactForm


def index(request):
    return render(request, 'blog/index.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form':form
            }
            messages.success(request, 'Formulario cargado exitosamente. Muchas gracias!')
            return render(request, 'contact.html', context)
    else:
        form = ContactForm()
        
    context = {
        'form':form
    }
    
    return render(request, 'contact.html', context)

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




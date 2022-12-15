from django.shortcuts import render, redirect
from .forms import CustomerUserForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})      

def create_users(request):
    context = {
        'form':CustomerUserForm
    }   
    
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect(to='index')   

    return render(request, 'registration/create_users.html', context)  


def denuncias(request):
    pass
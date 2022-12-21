from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from blog.forms import ContactForm
from blog.models import News


def index(request):
    new = News.objects.all().order_by('date')
    news = News.objects.filter(title__contains=request.GET.get('search','')).order_by('-date')
    print(news)
    context = {
        'news':news,
        'new':new
    }

    return render(request, 'blog/index.html', context)

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
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user) 
            return redirect(to='blog')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
        }
    return render(request, 'registration/register.html', context)

def about(request):
    return render(request, 'about.html')


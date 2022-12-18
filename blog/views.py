from django.shortcuts import render, redirect
from django.contrib import messages
from .models import News, CommentNews
from .forms import NewsForm, CommentNewsForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    news = News.objects.filter(title__contains=request.GET.get('search',''))
    
    context = {
        'news':news
    }

    return render(request, 'blog/index.html', context)

def view(request, id):
    blog = News.objects.get(id=id)
    context = {
        'blog':blog,
    }
    return render(request, 'blog/detail.html', context)

def edit(request, id):
    news = News.objects.get(id=id)
    if request.method == 'GET':        
        form = NewsForm(instance=news)
        context = {
            'form':form,
            'id':id
        }
        return render(request, 'blog/edit.html', context)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, instance= news, files=request.FILES)
        if form.is_valid():
            form.save()
        
        context = {
            'form':form,
            'id':id
        }
        messages.success(request, 'Noticia Actualizada!')
        return render(request, 'blog/edit.html', context)


def create(request):    
    if request.method == 'GET':
        form = NewsForm()
        context = {
            'form':form
        }
        return render(request, 'blog/create.html', context)

    if request.method == 'POST':
        form = NewsForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Noticia creada!')

        return redirect(to='blog')


def delete(request, id):
    news = News.objects.get(id=id)
    if request.method == 'GET':        
        form = NewsForm(instance=news)
        context = {
            'form':form,
            'id':id
        }
        return render(request, 'blog/delete.html', context)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news.delete()
        return redirect(to='blog')
"""
@login_required
def comment(request, id):
    form = CommentNews.objects.get(id=id)

    if request.method == 'GET':
        context = {
        'form':form
        }
        return render(request, 'blog/comment.html', context)

    if request.method == 'POST':
        form = CommentNewsForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            
        return redirect(to='blog')
"""        
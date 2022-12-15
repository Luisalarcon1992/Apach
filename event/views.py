from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.contrib import messages


def index(request):
    events = Event.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'events':events
    }
    return render(request, 'event/index.html', context)

def view(request, id):
    events = Event.objects.get(id=id)
    context = {
        'events':events
    }
    return render(request, 'event/detail.html', context)

def edit(request, id):
    event = Event.objects.get(id=id)

    if request.method == 'GET':
        form = EventForm(instance=event)
        context = {
            'form':form,
            'id':id
        }
        return render(request, 'event/edit.html', context)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()

        context = {
            'form':form,
            'id':id
        }
        messages.success(request, 'Evento Actualizado!')
        return render(request, 'event/edit.html', context)


def delete(request, id):
    event = Event.objects.get(id=id)
    if request.method == 'GET':
        form = EventForm(instance=event)
        context = {
            'form':form,
            'id':id
        }
        return render(request, 'event/delete.html', context)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event.delete()
    
        return redirect(to='event')

def create(request):
    if request.method == 'GET':
        form = EventForm()
        context = {
            'form':form
        }
        return render(request, 'event/create.html', context)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(to='event')
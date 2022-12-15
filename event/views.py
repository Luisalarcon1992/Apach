from django.shortcuts import render
from .models import Event


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
    pass

def delete(request, id):
    pass

def create(request):
    pass    
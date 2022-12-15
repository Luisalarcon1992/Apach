from django.forms import ModelForm
from .models import Event, MoreDetailEvent


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('date',)
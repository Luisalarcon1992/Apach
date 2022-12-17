from django.forms import ModelForm, DateInput
from .models import Event, MoreDetailEvent


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('date',)   
        widgets = {
            'date_event': DateInput(attrs={'type':'date'}),
        }  
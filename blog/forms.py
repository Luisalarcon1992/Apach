from django.forms import ModelForm
from .models import Contact, News

class NewsForm(ModelForm):
    class Meta:
        model = News
        exclude = ('date',)        


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)      


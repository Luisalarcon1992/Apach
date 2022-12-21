from django.forms import ModelForm
from django import forms
from .models import Contact, News, CommentNew

class NewsForm(ModelForm):
    class Meta:
        model = News
        exclude = ('date',)        


class ContactForm(ModelForm):   
    class Meta:
        model = Contact
        exclude = ('date',)   

class CommentNewForm(ModelForm):
    name = forms.CharField(max_length=100, label='Nombre ')
    comment_news = forms.CharField(label='Comentario ', widget=forms.Textarea)
    class Meta:
        model = CommentNew
        exclude = ('date_created','user')


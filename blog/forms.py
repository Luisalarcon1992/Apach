from django.forms import ModelForm
from .models import Contact, News, CommentNews

class NewsForm(ModelForm):
    class Meta:
        model = News
        exclude = ('date',)        


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)   

class CommentNewsForm(ModelForm):
    class Meta:
        model = CommentNews
        exclude = ('date_created',)


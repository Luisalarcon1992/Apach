from django.forms import ModelForm
from .models import Contact, News, Denuncia

class NewsForm(ModelForm):
    class Meta:
        model = News
        exclude = ('date',)        


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)      


class DenunciaForm(ModelForm):
    class Meta:
        model = Denuncia
        #exclude = ('date',)
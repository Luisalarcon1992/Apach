from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    desactivate = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/images_news/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title

class CommentNew(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=False, blank=False, related_name='comment')
    comment_news = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment_news



class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    mail = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    phone = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, blank=False, null=False)
    date_event = models.DateField(auto_now_add=True,blank=False, null=False)
    image = models.ImageField(upload_to='media/images_events/)', blank=True, null=True)

    def __str__(self):
        return self.title


class MoreDetailEvent(models.Model):
    model = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    more_info = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.model.title
from django.db import models
from django.utils import timezone   

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title


class MoreDetailEvent(models.Model):
    model = models.ForeignKey(Event, on_delete=models.CASCADE)
    more_info = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.model.title
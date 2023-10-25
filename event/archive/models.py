from django.db import models
from events.models import Event

# Create your models here.
class Archive(models.Model):
    archive = models.ForeignKey(Event, on_delete=models.CASCADE)


    @classmethod
    def send_event_archive(cls, event:Event):
        event.is_archive = True
        event.save()

        archive = cls(event=event)
        archive.save()
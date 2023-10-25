from django.db import models
from django.apps import apps
from user.models import User
from message.models import Chat


class Event(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Waiting_Response', 'Waiting Response'),
        ('Pending', 'Pending')
    ]

    open_date = models.DateField()
    close_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=40, default='Open')
    related_users = models.ManyToManyField(User, related_name='received_events', blank=True)
    is_archive = models.BooleanField(default=False)

    @property
    def username(self):
        return self.user.username
    

class EventChat(Event):
    chats = models.ManyToManyField(Chat, related_name='chats', blank=True)


class EventFile(Event):
    upload_date = models.DateField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    
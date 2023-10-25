from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventViewChat(viewsets.ModelViewSet):
    serializer_class = EventSerializerChat
    queryset = EventChat.objects.all()


class EventViewFile(viewsets.ModelViewSet):
    serializer_class = EventSerializerFile
    queryset = EventFile.objects.all()
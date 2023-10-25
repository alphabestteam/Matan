from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User, Message

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

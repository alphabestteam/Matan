from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from message import views
from user.models import User


router = routers.DefaultRouter()
router.register(r'chat', views.ChatView, 'chat')
router.register(r'message', views.MessageView, 'message')


urlpatterns = [
    path('api/', include(router.urls)),
]
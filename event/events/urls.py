from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events import views


router = routers.DefaultRouter()
router.register(r'events', views.EventView, 'events')
router.register(r'events-chat', views.EventViewChat, 'events-chat')
router.register(r'events-file', views.EventViewFile, 'events-file')


urlpatterns = [
    path('api/', include(router.urls)),
]
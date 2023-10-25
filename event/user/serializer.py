from rest_framework import serializers
from user.models import User
from events.models import Event
from message.models import Chat
from events.serializer import EventSerializer
from django.db.models import Q


class UserSerializer(serializers.ModelSerializer):
    related = serializers.SerializerMethodField()
    chat= serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['unread_messages']

    def get_related(self, obj):
        user_id = obj.id
        related_events = Event.objects.filter(Q(user=user_id) | Q(related_users__in=[obj]))
        return EventSerializer(related_events, many=True).data
    
    def get_chat(self, obj):
        if obj.chats is not None:
            for chat in obj.chats.all():
                obj.set_chat(chat)
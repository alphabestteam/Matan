from rest_framework import serializers
from events.models import Event, EventChat, EventFile


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'



class EventSerializerChat(serializers.ModelSerializer):
    class Meta:
        model = EventChat
        fields = '__all__'



class EventSerializerFile(serializers.ModelSerializer):
    class Meta:
        model = EventFile
        fields = '__all__'
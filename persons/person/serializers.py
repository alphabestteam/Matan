from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person  # Specify the model to serialize
        fields = '__all__'  # Or specify specific fields you want to include

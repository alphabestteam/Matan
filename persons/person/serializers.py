from rest_framework import serializers
from .models import Person, Parent


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person  # Specify the model to serialize
        fields = '__all__'  # Or specify specific fields you want to include
    
    
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

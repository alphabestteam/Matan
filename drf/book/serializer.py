from rest_framework import serializers
from .models import Book

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookTitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
from django.db import models
from rest_framework import serializers
from datetime import datetime as dt


def validate_publish_date(self, value):
        """
        in our library we dont allow new books under one year
        """
        current_date = dt.now().date()
        flag = current_date - value
        if flag.days > 365:
            raise serializers.ValidationError()
        return value


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(validators=[validate_publish_date])
    id = models.CharField(max_length=13, unique=True, primary_key=True)

    def __str__(self):
        return self.title
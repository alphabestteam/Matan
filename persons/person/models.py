from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(max_length=9, primary_key=True)
    date_of_birth = models.DateField()
    city = models.CharField(max_length= 100)

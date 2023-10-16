from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateField()
    city = models.CharField(max_length= 100)


class Parent(Person):
    work_place = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    kids = models.ManyToManyField('self', symmetrical=False, related_name='parents')

from django.db import models, migrations
from django.core.validators import MaxValueValidator
from datetime import datetime


class Person(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateField()
    city = models.CharField(max_length= 100)

    def is_over_18_method(self) -> bool:
        """
        this function checks if a person is over 18 or not
        input: None
        return: Bool
        """
        today = datetime.now().date()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

        return age > 18


class Parent(Person):
    work_place = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    kids = models.ManyToManyField('Person', blank=True, null=True,  related_name='parents')

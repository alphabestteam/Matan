from django.test import TestCase
from .models import Person
from datetime import datetime

# Create your tests here.
class YourModelTestCase(TestCase):
    def test_model_method(self):
        birthdate_str1 = '1990-05-15'
        birthdate_date1 = datetime.strptime(birthdate_str1, '%Y-%m-%d').date()
        test1 = Person.objects.create(name='Test1', date_of_birth = birthdate_date1, city = "Haifa")

        birthdate_str2 = '2007-05-15'
        birthdate_date2 = datetime.strptime(birthdate_str2, '%Y-%m-%d').date()
        test2 = Person.objects.create(name='Test1', date_of_birth = birthdate_date2, city = "Haifa")

        self.assertEqual(test1.is_over_18_method(), True)
        self.assertEqual(test2.is_over_18_method(), False)
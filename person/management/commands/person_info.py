import json
from typing import Any
from django.core.management.base import BaseCommand
from person.models import Person
from datetime import date


class Command(BaseCommand):
    help = "generate a json with name and age"

    def handle(self, *args: Any, **options: Any) -> str | None:
        all_people = Person.objects.all()
        current_date = date.today()
        count = 0

        for person in all_people:
            count += 1
            my_dict = {
                "name": person.name,
                "age_years": current_date.year - person.date_of_birth.year,
                "age_month": abs(current_date.month - person.date_of_birth.month)
            }
            fixture_filename = f'person_info{count}.json'
            with open(fixture_filename, 'w') as fixture_file:
                json.dump(my_dict, fixture_file, indent=2)

        self.stdout.write(self.style.SUCCESS(f'Fixture "{fixture_filename}" has been created.'))
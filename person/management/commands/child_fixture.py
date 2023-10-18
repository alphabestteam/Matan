import json
from typing import Any
from django.core.management.base import BaseCommand
from person.models import Parent
from person.serializers import PersonSerializer


class Command(BaseCommand):
    help = "generate a fixture for all of the children in the db"

    def handle(self, *args: Any, **options: Any) -> str | None:
        all_parents = Parent.objects.all()
        data_list = []

        for parent in all_parents:
            for kid in parent.kids.all():
                person_dict = PersonSerializer(kid).data
                if person_dict not in data_list:
                    data_list.append(person_dict)

        fixture_filename = 'children_fixture.json'

        with open(fixture_filename, 'w') as fixture_file:
            json.dump(data_list, fixture_file, indent=2)

        self.stdout.write(self.style.SUCCESS(f'Fixture "{fixture_filename}" has been created.'))
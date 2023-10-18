from typing import Any
from django.core.management.base import BaseCommand
from person.models import Parent
from datetime import date


class Command(BaseCommand):
    help = "give a raise to parents"

    def handle(self, *args: Any, **options: Any) -> str | None:
        all_parents = Parent.objects.all()
        count = 0
        
        for parent in all_parents:
            count += 1
            old_salary = parent.salary
            kid_count = parent.kids.count()
            if kid_count > 3:
                raise_num = 1800
            else: 
                raise_num = kid_count * 500

            parent.salary += raise_num
            parent.save()
            with open(f'client{count}.txt', 'w') as fixture_file:
                fixture_file.write(f"name: {parent.name}\n")
                fixture_file.write(f"number of kids: {kid_count}\n")
                fixture_file.write(f"old salary: {old_salary}\n")
                fixture_file.write(f"new salary: {parent.salary}\n")
                fixture_file.write(f"total salary: {parent.salary - old_salary}\n")

        self.stdout.write(self.style.SUCCESS('Raise has been done!'))
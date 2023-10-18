import json
from typing import Any
from django.core.management.base import BaseCommand
from person.models import Parent
from datetime import date


class Command(BaseCommand):
    help = "give a raise to parents"

    def handle(self, *args: Any, **options: Any) -> str | None:
        all_parents = Parent.objects.all()
        
        for parent in all_parents:
            kid_count = parent.kids.count()
            if kid_count > 3:
                raise_num = 1800
            else: 
                raise_num = kid_count * 500

            parent.salary += raise_num
            parent.save()

        self.stdout.write(self.style.SUCCESS('Raise has been done!'))
from django.db import migrations, models
from django.core.validators import MaxValueValidator

def change_field_type(apps, schema_editor):
    YourModel = apps.get_model('person', 'parent')

    # Iterate through all objects and change the field type
    for obj in YourModel.objects.all():
        obj.salary = int(obj.salary)
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_alter_parent_kids'),
    ]

    operations = [
        migrations.AlterField(  # Add a new IntegerField
            model_name='parent',
            name='salary',
            field=models.IntegerField(validators=[MaxValueValidator(999999)], null=True),  # Removed the inner list
        ),
        migrations.RunPython(change_field_type),  # Run the data migration
    ]

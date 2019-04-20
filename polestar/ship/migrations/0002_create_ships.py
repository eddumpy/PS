# coding=utf-8
from django.db import migrations


def create_ships(apps, schema_editor):

    Ship = apps.get_model('ship', 'Ship')

    ships = [
        (9632179, 'Mathilde Maersk​'),
        (9247455, 'Australian Spirit'),
        (9595321, 'MSC Preziosa')
    ]

    for ship in ships:
        Ship.objects.create(imo_number=ship[0], name=ship[1])


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_ships)
    ]

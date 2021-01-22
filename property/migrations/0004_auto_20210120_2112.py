# Generated by Django 2.2.4 on 2021-01-20 18:12
from django.db import migrations


def fill_new_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year > 2015:
            flat.new_building = True
        elif flat.construction_year <= 2015:
            flat.new_building = False
        else:
            continue
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_buildings)
    ]

# Generated by Django 2.2.4 on 2021-01-21 22:04
from django.db import migrations


def fill_flats_into_owners(apps, schema_editor):
    Owners = apps.get_model('property', 'Owner')
    Flats = apps.get_model('property', 'Flat')
    for owner in Owners.objects.all():
        flats = list(Flats.objects.filter(owner=owner.owner))
        owner.owned_flats.set(flats, clear=True)


def move_backward(apps, schema_editor):
    Owners = apps.get_model('property', 'Owner')
    for owner in Owners.objects.all():
        owner.owned_flats.set([], clear=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20210121_2202'),
    ]

    operations = [
        migrations.RunPython(fill_flats_into_owners, move_backward)
    ]

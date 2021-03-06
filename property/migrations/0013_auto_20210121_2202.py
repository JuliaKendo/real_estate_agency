# Generated by Django 2.2.4 on 2021-01-21 19:02

from django.db import migrations


def fill_owners(apps, schema_editor):
    Owners = apps.get_model('property', 'Owner')
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        Owners.objects.get_or_create(
            owner=flat.owner,
            defaults={
                'owners_phonenumber': flat.owners_phonenumber,
                'owner_pure_phone': flat.owner_pure_phone
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owners)
    ]

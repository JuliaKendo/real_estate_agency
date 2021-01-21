# Generated by Django 2.2.4 on 2021-01-21 13:17
import pdb
import phonenumbers
from django.db import migrations


def fill_owner_pure_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if not flat.owners_phonenumber:
            continue
        pure_phonenumber = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if not phonenumbers.is_valid_number(pure_phonenumber):
            continue
        flat.owner_pure_phone = phonenumbers.format_number(
            pure_phonenumber, phonenumbers.PhoneNumberFormat.E164
        )
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if not flat.owner_pure_phone:
            continue
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210121_1557'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phones, move_backward)
    ]

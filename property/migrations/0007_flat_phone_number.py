# Generated by Django 2.2.4 on 2021-01-21 12:45

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]

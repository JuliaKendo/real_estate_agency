# Generated by Django 2.2.4 on 2021-01-24 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20210122_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(choices=[(None, 'не заполнено'), (True, 'новостройка'), (False, 'старое здание')], db_index=True),
        ),
    ]
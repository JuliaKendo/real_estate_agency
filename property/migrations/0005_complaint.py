# Generated by Django 2.2.4 on 2021-01-20 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20210120_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_text', models.TextField(blank=True, verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Flat', verbose_name='Квартира на которую пожаловались')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]

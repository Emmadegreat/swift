# Generated by Django 5.0.4 on 2024-04-26 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swiftapp', '0011_useritems_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useritems',
            name='duration',
        ),
    ]
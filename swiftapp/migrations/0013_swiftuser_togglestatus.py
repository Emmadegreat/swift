# Generated by Django 5.0.4 on 2024-04-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftapp', '0012_remove_useritems_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='swiftuser',
            name='ToggleStatus',
            field=models.BooleanField(default=False),
        ),
    ]

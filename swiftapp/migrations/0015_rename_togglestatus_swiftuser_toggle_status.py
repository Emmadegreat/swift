# Generated by Django 5.0.4 on 2024-04-27 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swiftapp', '0014_showelement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swiftuser',
            old_name='ToggleStatus',
            new_name='toggle_status',
        ),
    ]

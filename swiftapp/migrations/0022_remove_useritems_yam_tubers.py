# Generated by Django 5.0.4 on 2024-04-30 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swiftapp', '0021_alter_useritems_yam_tubers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useritems',
            name='yam_tubers',
        ),
    ]
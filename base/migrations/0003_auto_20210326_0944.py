# Generated by Django 3.1.2 on 2021-03-26 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210326_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bluelane',
            old_name='blue_green_stop_name',
            new_name='blue_stop_name',
        ),
    ]

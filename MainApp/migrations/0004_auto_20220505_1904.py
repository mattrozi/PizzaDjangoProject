# Generated by Django 3.0.5 on 2022-05-06 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20220505_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='topping_name',
            new_name='text',
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-08 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_membership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='lname',
            new_name='last_name',
        ),
    ]
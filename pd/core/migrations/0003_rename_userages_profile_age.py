# Generated by Django 4.1.7 on 2023-06-05 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_userages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userages',
            new_name='age',
        ),
    ]

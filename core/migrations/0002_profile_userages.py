# Generated by Django 4.1.7 on 2023-06-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userages',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

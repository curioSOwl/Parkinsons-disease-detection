# Generated by Django 4.1.7 on 2023-06-07 14:06

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_profile_location_profile_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('desc', models.TextField()),
                ('voice', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]

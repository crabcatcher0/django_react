# Generated by Django 5.0.2 on 2024-02-26 10:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='prodimages/'),
            preserve_default=False,
        ),
    ]

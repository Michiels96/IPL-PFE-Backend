# Generated by Django 3.0 on 2019-12-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20191206_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
    ]

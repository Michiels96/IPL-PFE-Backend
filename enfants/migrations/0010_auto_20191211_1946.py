# Generated by Django 3.0 on 2019-12-11 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enfants', '0009_auto_20191211_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infosupplementaire',
            old_name='scolarité',
            new_name='scolarite',
        ),
    ]
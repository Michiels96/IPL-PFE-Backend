# Generated by Django 3.0 on 2019-12-04 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_question', '0004_auto_20191204_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_staisfaction',
            new_name='note_statisfaction',
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-07 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votex',
            new_name='votes',
        ),
    ]
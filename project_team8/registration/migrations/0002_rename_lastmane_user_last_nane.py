# Generated by Django 4.2.5 on 2024-01-31 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lastmane',
            new_name='last_nane',
        ),
    ]
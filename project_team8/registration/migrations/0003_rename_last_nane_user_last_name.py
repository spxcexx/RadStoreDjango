# Generated by Django 4.2.5 on 2024-01-31 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_rename_lastmane_user_last_nane'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_nane',
            new_name='last_name',
        ),
    ]

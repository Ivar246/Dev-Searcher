# Generated by Django 4.1.3 on 2022-11-10 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skiill'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skiill',
            new_name='Skill',
        ),
    ]
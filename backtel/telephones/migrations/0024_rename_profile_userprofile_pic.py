# Generated by Django 5.1.4 on 2024-12-27 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telephones', '0023_alter_department_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile',
            new_name='pic',
        ),
    ]

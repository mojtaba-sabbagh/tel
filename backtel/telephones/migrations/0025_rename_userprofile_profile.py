# Generated by Django 5.1.4 on 2024-12-27 19:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telephones', '0024_rename_profile_userprofile_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]
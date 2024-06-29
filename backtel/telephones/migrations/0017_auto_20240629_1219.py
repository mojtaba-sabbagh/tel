# Generated by Django 3.2.25 on 2024-06-29 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telephones', '0016_rename_profile_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['dep_title'], 'verbose_name': 'واحد سازمانی', 'verbose_name_plural': 'واحدهای سازمانی'},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='dep_name',
            new_name='name',
        ),
    ]

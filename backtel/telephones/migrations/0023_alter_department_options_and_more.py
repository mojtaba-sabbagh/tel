# Generated by Django 5.1.4 on 2024-12-27 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telephones', '0022_alter_assign_options_alter_department_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['dep_title', 'dep_name'], 'verbose_name': 'واحد سازمانی', 'verbose_name_plural': 'واحدهای سازمانی'},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='address',
            new_name='dep_address',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='dep_name',
        ),
    ]

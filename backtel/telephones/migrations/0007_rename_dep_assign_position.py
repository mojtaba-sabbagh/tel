# Generated by Django 4.0.4 on 2022-06-19 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telephones', '0006_position_duties_alter_department_dep_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assign',
            old_name='dep',
            new_name='position',
        ),
    ]
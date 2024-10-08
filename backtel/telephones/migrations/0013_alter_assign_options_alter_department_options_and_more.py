# Generated by Django 5.0.7 on 2024-09-19 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("telephones", "0012_alter_position_options_alter_department_dep_title"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="assign",
            options={
                "ordering": ["tel"],
                "verbose_name": "تخصیص تلفن",
                "verbose_name_plural": "تخصیص تلفن\u200cها",
            },
        ),
        migrations.AlterModelOptions(
            name="department",
            options={
                "ordering": ["dep_title", "dep_name"],
                "verbose_name": "واحد سازمانی",
                "verbose_name_plural": "واحدهای سازمانی",
            },
        ),
        migrations.AlterModelOptions(
            name="position",
            options={
                "ordering": ["dep", "position_type", "owner"],
                "verbose_name": "پست سازمانی",
                "verbose_name_plural": "پست\u200cهای سازمانی",
            },
        ),
        migrations.AlterModelOptions(
            name="positiontype",
            options={
                "ordering": ["title"],
                "verbose_name": "نوع پست سازمانی",
                "verbose_name_plural": "انواع پست های سازمانی",
            },
        ),
        migrations.AlterModelOptions(
            name="profile",
            options={
                "ordering": ["last_name"],
                "verbose_name": "مشخصات کاربر",
                "verbose_name_plural": "مشخصات کاربران",
            },
        ),
        migrations.AlterModelOptions(
            name="telephone",
            options={
                "ordering": ["extension"],
                "verbose_name": "تلفن داخلی",
                "verbose_name_plural": "تلفن\u200cهای داخلی",
            },
        ),
    ]

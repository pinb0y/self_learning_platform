# Generated by Django 5.1.4 on 2024-12-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_test", "0004_testtry_points_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="number",
            field=models.PositiveSmallIntegerField(
                default=1,
                help_text="Укажите порядковый номер вопроса",
                verbose_name="Порядковый номер вопроса",
            ),
        ),
    ]

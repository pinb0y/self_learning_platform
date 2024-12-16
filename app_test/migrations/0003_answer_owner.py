# Generated by Django 5.1.4 on 2024-12-09 21:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_test", "0002_alter_test_linked_material_alter_test_name_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите создателя ответа",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель ответа",
            ),
        ),
    ]

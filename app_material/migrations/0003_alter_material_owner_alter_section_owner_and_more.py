# Generated by Django 5.1.4 on 2024-12-09 20:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_material', '0002_alter_subscription_section'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='owner',
            field=models.ForeignKey(
                blank=True,
                help_text='Укажите автора',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='materials',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор',
            ),
        ),
        migrations.AlterField(
            model_name='section',
            name='owner',
            field=models.ForeignKey(
                blank=True,
                help_text='Укажите автора',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='sections',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор',
            ),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='owner',
            field=models.ForeignKey(
                blank=True,
                help_text='Укажите пользователя подписки',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='subscriptions',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Пользователь',
            ),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-06 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название раздела', max_length=100, verbose_name='Название раздела')),
                ('description', models.CharField(blank=True, help_text='Напишите краткое описание', max_length=500, null=True, verbose_name='Краткое описание раздела')),
                ('preview', models.ImageField(blank=True, help_text='Добавьте картинку раздела', null=True, upload_to='app_material/section/preview', verbose_name='Картинка раздела')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания раздела')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения раздела')),
                ('is_published', models.BooleanField(default=True, help_text='укажите статус публичности', verbose_name='Статус публичности')),
                ('owner', models.ForeignKey(help_text='Укажите автора', on_delete=django.db.models.deletion.CASCADE, related_name='sections', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название статьи', max_length=100, verbose_name='Название статьи')),
                ('description', models.CharField(blank=True, help_text='Напишите краткое описание', max_length=500, null=True, verbose_name='Краткое описание статьи')),
                ('body', models.TextField(help_text='Введите текст статьи', verbose_name='Текст статьи')),
                ('preview', models.ImageField(blank=True, help_text='Добавьте картинку статьи', null=True, upload_to='app_material/material/preview', verbose_name='Картинка материала')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения статьи')),
                ('is_published', models.BooleanField(default=True, help_text='укажите статус публичности', verbose_name='Статус публичности')),
                ('owner', models.ForeignKey(help_text='Укажите автора', on_delete=django.db.models.deletion.CASCADE, related_name='materials', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('section', models.ForeignKey(help_text='Укажите Раздел статьи', on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='app_material.section', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения подписки')),
                ('is_active', models.BooleanField(default=False, help_text='укажите статус активности', verbose_name='Статус активности')),
                ('owner', models.ForeignKey(help_text='Укажите пользователя подписки', on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('section', models.ForeignKey(blank=True, help_text='Укажите материал для подписки', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='app_material.section', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ('id',),
            },
        ),
    ]

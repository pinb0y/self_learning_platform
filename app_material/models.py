from django.db import models

from app_material.services import generate_unique_slug
from app_user.models import User


class Section(models.Model):
    title = models.CharField(
        verbose_name='Название раздела',
        max_length=100,
        help_text='Введите название раздела'
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            generate_unique_slug(Material, self.title)
        super().save(*args, **kwargs)

    description = models.CharField(
        verbose_name='Краткое описание раздела',
        max_length=500,
        help_text='Напишите краткое описание',
        blank=True,
        null=True
    )
    preview = models.ImageField(
        verbose_name='Картинка раздела',
        upload_to='app_material/section/preview',
        help_text='Добавьте картинку раздела',
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='sections',
        help_text='Укажите автора',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания раздела',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения раздела',
        auto_now=True
    )
    is_published = models.BooleanField(
        verbose_name='Статус публичности',
        default=True,
        help_text='укажите статус публичности'
    )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ('id',)

    def __str__(self):
        return f'{self.title}'


class Material(models.Model):
    title = models.CharField(
        verbose_name='Название статьи',
        max_length=100,
        help_text='Введите название статьи'
    )

    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            generate_unique_slug(Material, self.title)
        super().save(*args, **kwargs)

    description = models.CharField(
        verbose_name='Краткое описание статьи',
        max_length=500,
        help_text='Напишите краткое описание',
        blank=True,
        null=True
    )
    body = models.TextField(
        verbose_name='Текст статьи',
        help_text='Введите текст статьи'
    )
    preview = models.ImageField(
        verbose_name='Картинка материала',
        upload_to='app_material/material/preview',
        help_text='Добавьте картинку статьи',
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='materials',
        help_text='Укажите автора',
        blank=True,
        null=True
    )
    section = models.ForeignKey(
        Section,
        verbose_name='Раздел',
        on_delete=models.CASCADE,
        related_name='materials',
        help_text='Укажите Раздел статьи'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания статьи',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения статьи',
        auto_now=True
    )
    is_published = models.BooleanField(
        verbose_name='Статус публичности',
        default=True,
        help_text='укажите статус публичности'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('id',)

    def __str__(self):
        return f'{self.title}'


class Subscription(models.Model):
    section = models.ForeignKey(
        Section,
        verbose_name='Раздел',
        on_delete=models.CASCADE,
        related_name='subscriptions',
        help_text='Укажите раздел для подписки',
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='subscriptions',
        help_text='Укажите пользователя подписки',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата подписки',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения подписки',
        auto_now=True
    )
    is_active = models.BooleanField(
        verbose_name='Статус активности',
        default=False,
        help_text='укажите статус активности'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('id',)

    def __str__(self):
        return f'{self.section} - {self.owner}'

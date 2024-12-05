from django.db import models

from app_material.models import Material, Section
from app_user.models import User


class Test(models.Model):
    Name = models.CharField(verbose_name='Название Теста', max_length=100, help_text='Введите название теста')
    Description = models.TextField(verbose_name='Описание теста', help_text='Введите описание теста', null=True,
                                   blank=True)
    preview = models.ImageField('Картинка теста', upload_to='app_test/test/preview',
                                help_text='Добавьте картинку теста', null=True, blank=True)
    linked_section = models.ForeignKey(Section, verbose_name='Связанный раздел', on_delete=models.CASCADE,
                                       help_text='Укажите связанный раздел', null=True, blank=True)
    linked_material = models.ForeignKey(Material, verbose_name='Связанный материал', on_delete=models.CASCADE,
                                        help_text='Укажите связанный раздел', null=True, blank=True)
    owner = models.ForeignKey(User, verbose_name='Создатель теста', on_delete=models.CASCADE,
                              help_text='Укажите создателя теста', null=True, blank=True)
    questions_quantity = models.PositiveSmallIntegerField(verbose_name='Количество вопросов в тесте', default=10,
                                                          help_text='Укажите количество вопросов в тексте')
    lead_time = models.PositiveSmallIntegerField(verbose_name='Время на выполнение теста в минутах', default=10,
                                                 help_text='Укажите количество минут на выполнение теста')
    points_to_success = models.PositiveSmallIntegerField(verbose_name='Количество баллов для успешного прохождения',
                                                         default=90,
                                                         help_text='Укажите количество баллов для успешного прохождения')
    created_at = models.DateTimeField(verbose_name='Дата создания теста', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения теста', auto_now=True)
    is_published = models.BooleanField(verbose_name='Статус публичность', default=True,
                                       help_text='укажите статус публичности')


class Question(models.Model):
    ...


class Answer(models.Model):
    ...


class TestTry(models.Model):
    ...

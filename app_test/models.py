from django.db import models

from app_material.models import Material, Section
from app_user.models import User


class Test(models.Model):
    name = models.CharField(
        verbose_name='Название теста',
        max_length=100,
        help_text='Введите название теста'
    )
    description = models.TextField(
        verbose_name='Описание теста',
        help_text='Введите описание теста',
        null=True,
        blank=True)
    preview = models.ImageField(
        verbose_name='Картинка теста',
        upload_to='app_test/test/preview',
        help_text='Добавьте картинку теста',
        null=True,
        blank=True
    )
    linked_section = models.ForeignKey(
        Section,
        verbose_name='Связанный раздел',
        on_delete=models.CASCADE,
        related_name='tests',
        help_text='Укажите связанный раздел',
        null=True,
        blank=True)
    linked_material = models.ForeignKey(
        Material,
        verbose_name='Связанный материал',
        on_delete=models.CASCADE,
        related_name='tests',
        help_text='Укажите связанный материал',
        null=True,
        blank=True)
    owner = models.ForeignKey(
        User,
        verbose_name='Создатель теста',
        on_delete=models.CASCADE,
        related_name='tests',
        help_text='Укажите создателя теста',
        null=True,
        blank=True
    )
    questions_quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество вопросов в тесте',
        default=10,
        help_text='Укажите количество вопросов в тексте'
    )
    lead_time = models.PositiveSmallIntegerField(
        verbose_name='Время на выполнение теста в минутах',
        default=10,
        help_text='Укажите количество минут на выполнение теста'
    )
    points_to_success = models.PositiveSmallIntegerField(
        verbose_name='Количество баллов для успешного прохождения',
        default=90,
        help_text='Укажите количество баллов для успешного прохождения'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания теста',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения теста',
        auto_now=True
    )
    is_published = models.BooleanField(
        verbose_name='Статус публичности',
        default=True,
        help_text='укажите статус публичности'
    )

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    name = models.CharField(
        verbose_name='Название вопроса',
        max_length=100,
        help_text='Введите название вопроса'
    )
    body = models.TextField(
        verbose_name='Текст вопроса',
        help_text='Введите текст вопроса'
    )
    picture = models.ImageField(
        verbose_name='Картинка вопроса',
        upload_to='app_test/questions/picture',
        help_text='Добавьте картинку вопроса',
        null=True,
        blank=True
    )
    linked_test = models.ForeignKey(
        Test,
        verbose_name='Связанный тест',
        on_delete=models.CASCADE,
        related_name='questions',
        help_text='Выберете связанный тест'
    )
    points_per_answer = models.PositiveSmallIntegerField(
        verbose_name='Количество очков за ответ',
        default=10,
        help_text='Введите количество очков за правильный ответ'
    )
    answers_quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество вариантов ответа',
        default=4,
        help_text='Укажите количество правильных ответов'
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Создатель вопроса',
        on_delete=models.CASCADE,
        related_name='questions',
        help_text='Укажите создателя вопроса',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания вопроса',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения вопроса',
        auto_now=True
    )
    is_published = models.BooleanField(
        verbose_name='Статус публичности',
        default=True,
        help_text='укажите статус публичности'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'


class Answer(models.Model):
    short_answer = models.CharField(
        verbose_name='Краткий ответ',
        max_length=200,
        help_text='Введите краткий ответ'
    )
    full_answer = models.TextField(
        verbose_name='Полный текста ответа',
        help_text='Введите полный текст ответа',
        null=True,
        blank=True
    )
    picture = models.ImageField(
        verbose_name='Картинка ответа',
        upload_to='app_test/answer/picture',
        help_text='Добавьте картинку ответа',
        null=True,
        blank=True
    )
    linked_question = models.ForeignKey(
        Question,
        verbose_name='Связанный вопрос',
        on_delete=models.CASCADE,
        related_name='answers',
        help_text='Выберете связанный вопрос'
    )
    is_true = models.BooleanField(
        verbose_name='Статус верного ответа',
        default=False,
        help_text='Укажите является ли ответ верным'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания ответа',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения ответа',
        auto_now=True
    )
    is_published = models.BooleanField(
        verbose_name='Статус публичности',
        default=True,
        help_text='укажите статус публичности'
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('id',)

    def __str__(self):
        return f'{self.short_answer}'


class TestTry(models.Model):
    linked_test = models.ForeignKey(
        Test,
        verbose_name='Связанный тест',
        on_delete=models.CASCADE,
        related_name='test_tries',
        help_text='Укажите связанный тест'
    )
    linked_user = models.ForeignKey(
        User, verbose_name='Связанный пользователь',
        on_delete=models.CASCADE,
        related_name='test_tries',
        help_text='Укажите связанного пользователя'
    )
    right_answers_quantity = models.SmallIntegerField(
        verbose_name='Количество правильных ответов',
        default=0,
        help_text='Укажите количество правильных ответов'
    )
    is_passed = models.BooleanField(
        verbose_name='Статус успешности прохождения',
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания попытки прохождения теста',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения попытки прохождения теста',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Попытка сдачи теста'
        verbose_name_plural = 'Попытки сдачи теста'
        ordering = ('id',)

    def __str__(self):
        return f'{self.linked_test} - {self.linked_user}'

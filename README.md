### SELF LEARNING PLATFORM

Платформа для самообучения

### О проекте

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-DRF-464646?style=flat-square&logo=DRF)](https://https://www.django-rest-framework.org//)
[![Postgresql](https://img.shields.io/badge/-Postgresql-464646?style=flat-square&logo=Postgresql)](https://www.postgresql.org/)
[![CORS](https://img.shields.io/badge/-CORS-464646?style=flat-square&logo=CORS)](https://enable-cors.org//)

**Технологии:**

- **Django:** Основной фреймворк.
- **Django REST Framework (DRF):** Создание API.
- **PostgreSQL:** База данных.
- **CORS:** Взаимодействие с фронтенд-приложением.

#### Версия **Python 3.12**

### Функциональность

- Регистрация и аутентификация пользователей.
- Управление разделами и статьями и тестами
- Прохождение тестов по пройденному материалу
- Ведение статистики по пройденным тестам

### Установка и настройка

#### Клонируйте репозиторий:

```
https://github.com/pinb0y/self_learning_platform
```

#### Установите зависимости:

Для запуска проекта и установки зависимостей вам необходимо создать виртуальное окружение, с помощью команды

```
poetry install
```

#### Настройте базу данных в settings.py и выполните миграции:

```
python manage.py migrate
```

#### Загрузите из фикстуры роль учителя для админки

```
python manage.py loaddata groups.json
```

#### Настройка переменных окружения:

Создайте файл `.env` в корне проекта и заполните его переменными окружения указанными в файле `.env.example`.

#### Запустите проект

```
python manage.py runserver
```

### Прохождение теста

Ответы на тест принимаются `post` запросом по адресу:

```
http://127.0.0.1:8000/test/quiz/<quiz_id>/
```

в формате

```
{'answer': [номер правильного ответа 1, 2, 3, 4]}
```

В случае успешного прохождения выводит результаты. Если тест не пройден, выводит неверно отвеченные вопросы.

### Роли

1. Студент - любой новый пользователь по умолчанию. Может просматривать разделы, статьи и проходить тесты.
2. Учитель - Может создавать разделы, статьи и тесты. Вносить изменения в материалы. Чтобы сделать пользователя
   учителем, поставьте галочки в модели пользователя `is_staff` и `is_teacher`. Работает в админке и через API.
3. Администратор - Может все. Должна стоять галочка `is_staff` или `is_superuser`

### SWAGGER и REDOC

Документацию по API сформирована с помощью `drf-yasg`

- redoc```http://127.0.0.1:8000/redoc/```
- swagger```http://127.0.0.1:8000/docs/```

### CORS

CORS настроен для взаимодействия с фронтендом:

- Разрешён доступ с определённых доменов.
- Используется библиотека **django-cors-headers**.

Пинчук Сергей pinboyer@gmail.com
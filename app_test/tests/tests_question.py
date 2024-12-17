from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_test.models import Answer, Test, Question
from app_user.models import User


class QuestionModelTestCase(APITestCase):
    """Тест модели вопроса"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(email="testuser@test.test", password="test")
        self.test = Test.objects.create(owner=self.user, name="Тест по пиву")
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания вопроса"""

        question = Question.objects.create(
            owner=self.user,
            name="Самое крепкое пиво",
            body="Сколько стоит самое крепкое пиво?",
            linked_test=self.test,
        )

        self.assertEqual(question.owner, self.user)
        self.assertEqual(question.name, "Самое крепкое пиво")
        self.assertEqual(question.body, "Сколько стоит самое крепкое пиво?")
        self.assertEqual(question.linked_test, self.test)
        self.assertEqual(question.is_published, True)


class QuestionViewTestCase(APITestCase):
    """Тесты отображений Вопросов"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(
            email="testuser@test.test", password="test", is_teacher=True, is_staff=True
        )
        self.client.force_authenticate(user=self.user)
        self.test = Test.objects.create(
            owner=self.user,
            name="Тест по пиву",
            description="Базовое тестирование по разделу Пиво",
        )
        self.question = Question.objects.create(
            owner=self.user,
            name="Самое крепкое пиво",
            body="Сколько стоит самое крепкое пиво?",
            linked_test=self.test,
        )

    def test_question_retrieve(self):
        """Тестирование вывода одного вопроса"""

        url = reverse("app_test:question-detail", args=(self.question.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.question.name)

    def test_question_update(self):
        """Тестирование изменения одного вопроса"""

        url = reverse("app_test:question-detail", args=(self.question.pk,))
        data = {"name": "самое дешевое пиво"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "самое дешевое пиво")

    def test_question_create(self):
        """Тестирование создания вопроса"""

        url = reverse("app_test:question-create")
        data = {
            "name": "Зачем в пиве хмель",
            "body": "Зачем в пиво добавляют хмель?",
            "linked_test": self.test.pk,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.all().count(), 2)

    def test_question_list(self):
        """Тестирование вывода всех вопросов"""

        url = reverse("app_test:question-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "name": "Самое крепкое пиво",
                "body": "Сколько стоит самое крепкое пиво?",
                "linked_test": self.test.pk,
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_question_delete(self):
        """Тестирование удаления одного вопроса"""

        url = reverse("app_test:question-detail", args=(self.question.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.all().count(), 0)

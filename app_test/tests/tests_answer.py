from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_test.models import Answer, Test, Question
from app_user.models import User


class AnswerModelTestCase(APITestCase):
    """Тест модели ответа"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(email="testuser@test.test", password="test")
        self.test = Test.objects.create(owner=self.user, name="Тест по пиву")
        self.question = Question.objects.create(
            owner=self.user,
            name="Самое крепкое пиво",
            body="Сколько стоит самое крепкое пиво?",
            linked_test=self.test,
        )
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания ответа"""

        answer = Answer.objects.create(
            owner=self.user,
            short_answer="67%vol",
            full_answer="Самое крепкое пиво 67%vol",
            linked_question=self.question,
        )

        self.assertEqual(answer.owner, self.user)
        self.assertEqual(answer.short_answer, "67%vol")
        self.assertEqual(answer.full_answer, "Самое крепкое пиво 67%vol")
        self.assertEqual(answer.linked_question, self.question)
        self.assertEqual(answer.is_published, True)
        self.assertEqual(answer.is_true, False)


class AnswerViewTestCase(APITestCase):
    """Тесты отображений ответов"""

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
        self.answer = Answer.objects.create(
            owner=self.user,
            short_answer="67%vol",
            full_answer="Самое крепкое пиво 67%vol",
            linked_question=self.question,
        )

    def test_answer_retrieve(self):
        """Тестирование вывода одного ответа"""

        url = reverse("app_test:answer-detail", args=(self.answer.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("short_answer"), self.answer.short_answer)

    def test_answer_update(self):
        """Тестирование изменения одного ответа"""

        url = reverse("app_test:answer-detail", args=(self.answer.pk,))
        data = {"short_answer": "три писят"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("short_answer"), "три писят")

    def test_answer_create(self):
        """Тестирование создания ответа"""

        url = reverse("app_test:answer-create")
        data = {
            "owner": self.user.pk,
            "short_answer": "60%vol",
            "full_answer": "Самое крепкое пиво 60%vol",
            "linked_question": self.question.pk,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.all().count(), 2)

    def test_answer_list(self):
        """Тестирование вывода всех ответов"""

        url = reverse("app_test:answer-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "number": 1,
                "linked_question": self.question.pk,
                "short_answer": "67%vol",
                "full_answer": "Самое крепкое пиво 67%vol",
                "is_true": False,
            },
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_answer_delete(self):
        """Тестирование удаления одного ответа"""

        url = reverse("app_test:answer-detail", args=(self.answer.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Answer.objects.all().count(), 0)

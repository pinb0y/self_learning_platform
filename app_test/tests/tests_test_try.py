from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_test.models import Test, TestTry
from app_user.models import User


class TestTryModelTestCase(APITestCase):
    """Тест модели попытки теста"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(email="testuser@test.test", password="test")
        self.test = Test.objects.create(owner=self.user, name="Тест по пиву")
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания попытки теста"""

        test_try = TestTry.objects.create(
            linked_user=self.user,
            linked_test=self.test,
        )

        self.assertEqual(test_try.linked_user, self.user)
        self.assertEqual(test_try.linked_test, self.test)
        self.assertEqual(test_try.right_answers_quantity, 0)
        self.assertEqual(test_try.points_quantity, 0)
        self.assertEqual(test_try.is_passed, False)


class TestTryViewTestCase(APITestCase):
    """Тесты отображений попыток тестирования"""

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
        self.test_try = TestTry.objects.create(
            linked_user=self.user,
            linked_test=self.test,
        )

    def test_test_try_retrieve(self):
        """Тестирование вывода одной попытки теста"""

        url = reverse("app_test:test-try-detail", args=(self.test_try.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("is_passed"), False)

    def test_test_try_update(self):
        """Тестирование изменения одной попытки теста"""

        url = reverse("app_test:test-try-detail", args=(self.test_try.pk,))
        data = {"is_passed": True}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("is_passed"), True)

    def test_test_try_list(self):
        """Тестирование вывода всех попыток теста"""

        url = reverse("app_test:test-try-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.test_try.pk,
                "right_answers_quantity": 0,
                "points_quantity": 0,
                "is_passed": False,
                "linked_test": self.test.pk,
                "linked_user": self.user.pk,
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_test_try_delete(self):
        """Тестирование удаления одной попытки теста"""

        url = reverse("app_test:test-try-detail", args=(self.test_try.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TestTry.objects.all().count(), 0)

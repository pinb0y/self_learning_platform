from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_test.models import Test
from app_user.models import User


class TestModelTestCase(APITestCase):
    """Тест модели теста"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(email="testuser@test.test", password="test")
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания теста"""

        test = Test.objects.create(
            owner=self.user,
            name="Тест по пиву",
            description="Базовое тестирование по разделу Пиво",
        )

        self.assertEqual(test.owner, self.user)
        self.assertEqual(test.name, "Тест по пиву")
        self.assertEqual(test.description, "Базовое тестирование по разделу Пиво")
        self.assertEqual(test.is_published, True)


class TestViewTestCase(APITestCase):
    """Тесты отображений тестов"""

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

    def test_test_retrieve(self):
        """Тестирование вывода одного теста"""

        url = reverse("app_test:test-detail", args=(self.test.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.test.name)

    def test_test_update(self):
        """Тестирование изменения одного теста"""

        url = reverse("app_test:test-detail", args=(self.test.pk,))
        data = {"name": "Тест по светлому пиву"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Тест по светлому пиву")

    def test_test_create(self):
        """Тестирование создания теста"""

        url = reverse("app_test:test-create")
        data = {
            "name": "Тест по сидру",
            "description": "Общее тестирование по теме сидр",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Test.objects.all().count(), 2)

    def test_test_list(self):
        """Тестирование вывода всех разделов"""

        url = reverse("app_test:test-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "name": "Тест по пиву",
                "linked_section": None,
                "linked_material": None,
                "points_to_success": 90,
                "questions": [],
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_test_delete(self):
        """Тестирование удаления одного теста"""

        url = reverse("app_test:test-detail", args=(self.test.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Test.objects.all().count(), 0)

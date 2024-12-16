from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_material.models import Section
from app_user.models import User


class SectionModelTestCase(APITestCase):
    """Тест модели раздела"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(email="testuser@test.test", password="test")
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания привычки"""

        section = Section.objects.create(
            owner=self.user,
            title="Пиво",
            description="Раздел о пиве",
        )

        self.assertEqual(section.owner, self.user)
        self.assertEqual(section.title, "Пиво")
        self.assertEqual(section.description, "Раздел о пиве")
        self.assertEqual(section.preview, None)
        self.assertEqual(section.is_published, True)


class SectionViewTestCase(APITestCase):
    """Тесты отображений раздела"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(
            email="testuser@test.test", password="test", is_teacher=True, is_staff=True
        )
        self.client.force_authenticate(user=self.user)
        self.section = Section.objects.create(
            owner=self.user,
            title="Пиво",
            slug="pivo",
            description="Раздел о пиве",
        )

    def test_section_retrieve(self):
        """Тестирование вывода одного раздела"""

        url = reverse("app_material:section-retrieve", args=(self.section.slug,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.section.title)

    def test_section_update(self):
        """Тестирование изменения одного раздела"""

        url = reverse("app_material:section-update", args=(self.section.slug,))
        data = {"description": "Раздел о великом пиве"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("description"), "Раздел о великом пиве")

    def test_section_create(self):
        """Тестирование создания раздела"""

        url = reverse("app_material:section-create")
        data = {
            "title": "Сидр",
            "description": "Раздел о сидре",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Section.objects.all().count(), 2)

    def test_section_list(self):
        """Тестирование вывода всех разделов"""

        url = reverse("app_material:section-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.section.id,
                "title": "Пиво",
                "slug": "pivo",
                "description": "Раздел о пиве",
                "preview": None,
                "owner": self.user.id,
                "materials": [],
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_section_delete(self):
        """Тестирование удаления одного раздела"""

        url = reverse("app_material:section-delete", args=(self.section.slug,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Section.objects.all().count(), 0)

# class SectionSerializerTestCase(APITestCase):
#     """Тестирование сериализатора раздела"""
#
#     def setUp(self):
#         """Фикстуры"""
#
#         self.user = User.objects.create(
#             email="testuser3@test.test", password="test", is_teacher=True, is_staff=True
#         )
#         self.section = Section.objects.create(
#             owner=self.user,
#             title="Пиво",
#             slug="pivo",
#             description="Раздел о пиве",
#         )
#
#     def test_valid_data(self):
#         """Проверка правильных значений сериализатора статьи"""
#         data = {
#             "id": self.section.id,
#             "title": "Пиво",
#             "slug": "pivo",
#             "description": "Раздел о пиве",
#             "preview": None,
#             "owner": self.user.id,
#             "materials": [],
#         }
#         serializer = SectionSerializer(data=data)
#         print(serializer)
#         self.assertTrue(serializer.is_valid())
#
#     def test_invalid_data(self):
#         """Проверка неправильных значений сериализатора статьи"""
#         data = {
#             "title": 112,
#             "slug": "pivofds",
#             "description": "Разделfff о пиве",
#             "materials": 23,
#         }
#         serializer = SectionSerializer(data=data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn("title", serializer.errors)
#         self.assertIn("slug", serializer.errors)
#         self.assertIn("description", serializer.errors)
#         self.assertIn("materials", serializer.errors)

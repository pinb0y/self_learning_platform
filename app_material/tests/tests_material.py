from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_material.models import Material, Section
from app_user.models import User


class MaterialModelTestCase(APITestCase):
    """Тест модели раздела"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(email="testuser@test.test", password="test")
        self.section = Section.objects.create(owner=self.user, title="Пиво")
        self.client.force_authenticate(user=self.user)

    def test_model(self):
        """Тест создания привычки"""

        material = Material.objects.create(
            owner=self.user,
            title="Классификация пива",
            description="Различные классификации пива",
            body="Если б было море пивом",
            section=self.section,
        )

        self.assertEqual(material.owner, self.user)
        self.assertEqual(material.title, "Классификация пива")
        self.assertEqual(material.description, "Различные классификации пива")
        self.assertEqual(material.body, "Если б было море пивом")
        self.assertEqual(material.section, self.section)
        self.assertEqual(material.is_published, True)


class MaterialViewTestCase(APITestCase):
    """Тесты отображений статьи"""

    def setUp(self):
        """Фикстуры"""

        self.user = User.objects.create(
            email="testuser2@test.test", password="test", is_teacher=True, is_staff=True
        )
        self.client.force_authenticate(user=self.user)
        self.section = Section.objects.create(
            owner=self.user,
            title="Пивас",
            slug="pivas",
            description="Раздел о пиве",
        )
        self.material = Material.objects.create(
            owner=self.user,
            title="Классификация пива",
            slug="klassifikaciya-piva",
            description="Различные классификации пива",
            body="Если б было море пивом",
            section=self.section,
        )

    def test_material_retrieve(self):
        """Тестирование вывода одной статьи"""

        url = reverse("app_material:material-retrieve", args=(self.material.slug,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.material.title)

    def test_material_update(self):
        """Тестирование изменения одной статьи"""

        url = reverse("app_material:material-update", args=(self.material.slug,))
        data = {"description": "Коротко о классификации пива"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("description"), "Коротко о классификации пива")

    def test_material_create(self):
        """Тестирование создания статьи"""

        url = reverse("app_material:material-create")
        data = {
            "title": "Стили пива",
            "description": "Статья о стилях пива",
            "body": "Если б было море пивом",
            "section": self.section.pk,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Material.objects.all().count(), 2)

    def test_material_list(self):
        """Тестирование вывода всех статей"""

        url = reverse("app_material:material-list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.material.id,
                "title": "Классификация пива",
                "slug": "klassifikaciya-piva",
                "description": "Различные классификации пива",
                "body": "Если б было море пивом",
                "preview": None,
                "is_published": True,
                "owner": self.user.pk,
                "section": self.section.pk,
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_material_delete(self):
        """Тестирование удаления одной статьи"""

        url = reverse("app_material:material-delete", args=(self.material.slug,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Material.objects.all().count(), 0)

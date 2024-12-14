from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from app_material.models import Section, Material
from app_material.serializers import SectionSerializer, MaterialSerializer
from app_user.models import User
from app_user.permissions import IsOwner, IsTeacher, IsAdmin


# __________________Section_______________________________

class SectionCreateAPIView(CreateAPIView):
    """Отображение для создания раздела"""
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        """При создании записывает в поле владельца текущего пользователя"""

        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class SectionListAPIView(ListAPIView):
    """Отображение для вывода списка разделов"""

    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionRetrieveAPIView(RetrieveAPIView):
    """Отображение для вывода раздела"""

    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    lookup_field = 'slug'


class SectionUpdateAPIView(UpdateAPIView):
    """Отображение для изменения раздела"""

    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'


class SectionDestroyAPIView(DestroyAPIView):
    """Отображение для удаления раздела"""

    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'


# __________________Material________________________

class MaterialCreateAPIView(CreateAPIView):
    """Отображение для создания статьи"""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        """При создании записывает в поле владельца текущего пользователя"""

        if isinstance(self.request.user, User):
            serializer.save(user=self.request.user)
        serializer.save()


class MaterialListAPIView(ListAPIView):
    """Отображение для вывода списка статей"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialRetrieveAPIView(RetrieveAPIView):
    """Отображение для вывода статьи"""

    serializer_class = MaterialSerializer
    queryset = Section.objects.all()
    lookup_field = 'slug'


class MaterialUpdateAPIView(UpdateAPIView):
    """Отображение для изменения статьи"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'


class MaterialDestroyAPIView(DestroyAPIView):
    """Отображение для удаления статьи"""

    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from app_material.models import Section, Material
from app_material.serializers import SectionSerializer, MaterialSerializer
from app_user.models import User
from app_user.permissions import IsOwner, IsTeacher, IsAdmin


# __________________Section_______________________________

class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class SectionListAPIView(ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    lookup_field = 'slug'


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'


# __________________Material________________________

class MaterialCreateAPIView(CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            serializer.save(user=self.request.user)
        serializer.save()


class MaterialListAPIView(ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialRetrieveAPIView(RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Section.objects.all()
    lookup_field = 'slug'


class MaterialUpdateAPIView(UpdateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'


class MaterialDestroyAPIView(DestroyAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
    lookup_field = 'slug'

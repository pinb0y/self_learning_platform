from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from app_material.models import Section, Material
from app_material.serializers import SectionSerializer, MaterialSerializer


# __________________Section_______________________________

class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionListAPIView(ListAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


# __________________Material________________________

class MaterialCreateAPIView(CreateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialListAPIView(ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialRetrieveAPIView(RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Section.objects.all()


class MaterialUpdateAPIView(UpdateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialDestroyAPIView(DestroyAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()

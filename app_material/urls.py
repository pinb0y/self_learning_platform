from django.urls import path

from app_material.apps import AppMaterialConfig
from app_material.views import SectionCreateAPIView, SectionDestroyAPIView, SectionUpdateAPIView, \
    SectionRetrieveAPIView, SectionListAPIView, MaterialCreateAPIView, MaterialListAPIView, MaterialUpdateAPIView, \
    MaterialDestroyAPIView, MaterialRetrieveAPIView

app_name = AppMaterialConfig.name

urlpatterns = [
    path('section/create/', SectionCreateAPIView.as_view(), name='section-create'),
    path('section/list/', SectionListAPIView.as_view(), name='section-list'),
    path('section/<int:pk>/', SectionRetrieveAPIView.as_view(), name='section-retrieve'),
    path('section/update/<int:pk>/', SectionUpdateAPIView.as_view(), name='section-update'),
    path('section/delete/<int:pk>/', SectionDestroyAPIView.as_view(), name='section-delete'),

    path('material/create/', MaterialCreateAPIView.as_view(), name='material-create'),
    path('material/list/', MaterialListAPIView.as_view(), name='material-list'),
    path('material/<int:pk>/', MaterialRetrieveAPIView.as_view(), name='material-retrieve'),
    path('material/update/<int:pk>/', MaterialUpdateAPIView.as_view(), name='material-update'),
    path('material/delete/<int:pk>/', MaterialDestroyAPIView.as_view(), name='material-delete'),
]
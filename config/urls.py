from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from config import settings

schema_view = get_schema_view(
    openapi.Info(
        title="API документация для платформы самообучения имени Сергея Пинчука",
        default_version="Версия 1",
        contact=openapi.Contact(email="pinboyer@gmail.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('app_user.urls', namespace='user')),
    path('', include('app_material.urls', namespace='section')),
    path('test/', include('app_test.urls', namespace='test')),

    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
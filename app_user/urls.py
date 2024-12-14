from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app_user.apps import AppUserConfig
from app_user.views import (
    UserCreateAPIView,
    UserListApiView,
    UserRetrieveApiView,
    UserUpdateApiView,
    UserDestroyApiView,
)
from config import settings

app_name = AppUserConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', UserListApiView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveApiView.as_view(), name='user-detail'),
    path('update/<int:pk>/', UserUpdateApiView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyApiView.as_view(), name='user-delete'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

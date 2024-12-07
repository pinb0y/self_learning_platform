from django.urls import path

from app_user.apps import AppUserConfig
from app_user.views import UserCreateAPIView, UserListApiView, UserRetrieveApiView, UserUpdateApiView, \
    UserDestroyApiView

app_name = AppUserConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', UserListApiView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveApiView.as_view(), name='user-detail'),
    path('update/<int:pk>/', UserUpdateApiView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyApiView.as_view(), name='user-delete'),
]

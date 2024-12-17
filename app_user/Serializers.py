from rest_framework import serializers

from app_test.serializers import TestTrySerializer
from app_user.models import User


class UserSerializer(serializers.ModelSerializer):
    test_tries = TestTrySerializer(many=True)

    class Meta:
        model = User
        fields = ("email", "telegram_nik", "is_teacher", "test_tries")


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )

from rest_framework import serializers

from app_material.models import Section, Material, Subscription


class MaterialSerializer(serializers.ModelSerializer):
    """Сериалайзер для отображения статей"""

    class Meta:
        model = Material
        exclude = ('created_at', 'updated_at')


class SectionSerializer(serializers.ModelSerializer):
    """Сериалайзер для отображения Материалов"""

    materials = MaterialSerializer(many=True)

    class Meta:
        model = Section
        fields = ('id', 'title', 'slug', 'description', 'preview', 'owner', 'materials')


# class SubscriptionSerializer(serializers.ModelSerializer):
#     """Сериалайзер для отображения подписок. Планируется в будущем"""
#
#     class Meta:
#         model = Subscription
#         exclude = ('created_at', 'updated_at')

from rest_framework import serializers

from app_material.models import Section, Material, Subscription


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        exclude = ('created_at', 'updated_at')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        exclude = ('created_at', 'updated_at')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ('created_at', 'updated_at')

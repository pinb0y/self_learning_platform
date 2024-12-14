from rest_framework import serializers

from app_material.models import Section, Material, Subscription



class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        exclude = ('created_at', 'updated_at')


class SectionSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True)


    class Meta:
        model = Section
        fields = ('id', 'title', 'slug', 'description', 'preview', 'owner', 'materials')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ('created_at', 'updated_at')

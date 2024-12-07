from rest_framework import serializers

from app_test.models import Test, Question, Answer, TestTry


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        exclude = ('created_at', 'updated_at')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ('created_at', 'updated_at')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ('created_at', 'updated_at')


class TestTrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTry
        exclude = ('created_at', 'updated_at')

from rest_framework import serializers

from app_test.models import Test, Question, Answer, TestTry


class AnswerSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели ответ"""

    class Meta:
        model = Answer
        fields = ('number', 'short_answer', 'full_answer', 'is_true',)


class QuestionSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели вопрос"""

    class Meta:
        model = Question
        fields = ('name', 'body')


class QuizQuestionSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода вопроса для теста"""

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('body', 'answers')


class TestSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели тест"""

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('name', 'linked_section', 'linked_material', 'points_to_success', 'questions',)


class QuizSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода теста"""

    questions = QuizQuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('name', 'questions')


class TestTrySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели попытки сдачи теста"""

    class Meta:
        model = TestTry
        exclude = ('created_at', 'updated_at')

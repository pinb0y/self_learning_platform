from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from app_test.models import Test, Question, Answer
from app_test.serializers import TestSerializer, QuestionSerializer, AnswerSerializer


# __________________Test________________________

class TestCreateAPIView(CreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestListAPIView(ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestRetrieveAPIView(RetrieveAPIView):
    serializer_class = TestSerializer
    queryset =Test.objects.all()


class TestUpdateAPIView(UpdateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestDestroyAPIView(DestroyAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


# __________________Question________________________

class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset =Question.objects.all()


class QuestionUpdateAPIView(UpdateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDestroyAPIView(DestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


# __________________Answer________________________

class AnswerCreateAPIView(CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class AnswerListAPIView(ListAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class AnswerRetrieveAPIView(RetrieveAPIView):
    serializer_class = AnswerSerializer
    queryset =Answer.objects.all()


class AnswerUpdateAPIView(UpdateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class AnswerDestroyAPIView(DestroyAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
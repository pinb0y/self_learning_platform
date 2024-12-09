from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from app_test.models import Test, Question, Answer
from app_test.serializers import TestSerializer, QuestionSerializer, AnswerSerializer
from app_user.models import User
from app_user.permissions import IsTeacher, IsAdmin, IsOwner


# __________________Test________________________

class TestCreateAPIView(CreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class TestListAPIView(ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestRetrieveAPIView(RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestUpdateAPIView(UpdateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


class TestDestroyAPIView(DestroyAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


# __________________Question________________________

class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner | IsAdmin,)

class QuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner | IsAdmin,)

class QuestionUpdateAPIView(UpdateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner | IsAdmin,)

class QuestionDestroyAPIView(DestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner | IsAdmin,)

# __________________Answer________________________

class AnswerCreateAPIView(CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

class AnswerListAPIView(ListAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsOwner | IsAdmin,)

class AnswerRetrieveAPIView(RetrieveAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsOwner | IsAdmin,)

class AnswerUpdateAPIView(UpdateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsOwner | IsAdmin,)

class AnswerDestroyAPIView(DestroyAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsOwner | IsAdmin,)
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from app_test.models import Test, Question, Answer, TestTry
from app_test.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, TestTrySerializer, QuizSerializer
from app_test.servises import check_answers, check_test_pass
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
    permission_classes = (IsOwner | IsAdmin,)


class TestRetrieveAPIView(RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


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


class TestAPIView(APIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def get(self, request, **kwargs):
        user = self.request.user

        test_item = get_object_or_404(Test, pk=kwargs['pk'])

        test_try, _ = TestTry.objects.get_or_create(linked_user=user, linked_test=test_item)
        serializer = QuizSerializer(test_item)

        response = serializer.data

        return Response(response, status.HTTP_201_CREATED)

    def post(self, request, pk):
        user = self.request.user
        user_answer = request.data.get('answers')
        test_item = get_object_or_404(Test, pk=pk)
        questions = Question.objects.filter(linked_test=test_item)
        test_try, _ = TestTry.objects.get_or_create(linked_user=user, linked_test=test_item)
        points_to_pass = test_item.points_to_success

        for answer_id, question in enumerate(questions):
            wrong_answers = []
            answer = Answer.objects.filter(linked_question=question).filter(is_true=True).first().number
            scores = question.points_per_answer
            wrong_answer = check_answers(question=question, user_answer=user_answer[answer_id], right_answer=answer,
                                         scores=scores, test_try=test_try)
            if wrong_answer:
                wrong_answers.append(wrong_answer)
        points = test_try.points_quantity

        check_test_pass(points=points, points_to_pass=points_to_pass, test_try=test_try)
        if test_try.is_passed:
            response = {
                'result': 'Тест успешно пройдет. Поздравляем!',
                'right_answers': f'Отвечено на {test_try.right_answers_quantity} из {test_item.questions_quantity}',
                'scores': f'Набрано {test_try.points_quantity} очков',
            }
        else:
            response = {
                'results': 'К сожалению тест не пройден',
                'wrong_answers_quantity': f'Вы ответили неправильно на {test_item.questions_quantity - test_try.right_answers_quantity} вопросов',
                'wrong_answers': f'Не отвеченные вопросы {wrong_answers}'
            }
        return Response(response, status.HTTP_200_OK)


class TestTryAPIView(ListAPIView):
    queryset = TestTry.objects.all()
    serializer_class = TestTrySerializer
    permission_classes = (IsOwner | IsAdmin,)


class TestTryRetrieveAPIView(RetrieveAPIView):
    queryset = TestTry.objects.all()
    serializer_class = TestTrySerializer
    permission_classes = (IsOwner | IsAdmin,)

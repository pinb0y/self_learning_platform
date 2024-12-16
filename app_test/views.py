from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    get_object_or_404,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from app_test.models import Test, Question, Answer, TestTry
from app_test.serializers import (
    TestSerializer,
    QuestionSerializer,
    AnswerSerializer,
    TestTrySerializer,
    QuizSerializer,
)
from app_test.servises import check_answers, check_test_pass
from app_user.models import User
from app_user.permissions import IsTeacher, IsAdmin, IsOwner


# __________________Test________________________


class TestCreateAPIView(CreateAPIView):
    """Отображение для создания теста"""

    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        """Привязывает текущего пользователя к полю владельца теста"""

        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class TestListAPIView(ListAPIView):
    """Отображение для вывода списка тестов"""

    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


class TestAPIView(RetrieveUpdateDestroyAPIView):
    """Отображение для вывода, изменения и удаления теста"""

    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


# __________________Question________________________


class QuestionCreateAPIView(CreateAPIView):
    """Отображение для создания вопроса"""

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        """Привязывает текущего пользователя к полю владельца вопроса"""

        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class QuestionListAPIView(ListAPIView):
    """Отображение для вывода списка вопросов"""

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


class QuestionAPIView(RetrieveUpdateDestroyAPIView):
    """Отображение для вывода, изменения и удаления вопроса"""

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


# __________________Answer________________________


class AnswerCreateAPIView(CreateAPIView):
    """Отображение для создания ответа"""

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsTeacher | IsAdmin,)

    def perform_create(self, serializer):
        """Привязывает текущего пользователя к полю владельца ответа"""

        if isinstance(self.request.user, User):
            serializer.save(owner=self.request.user)
        serializer.save()


class AnswerListAPIView(ListAPIView):
    """Отображение для вывода списка ответов"""

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


class AnswerAPIView(RetrieveUpdateDestroyAPIView):
    """Отображение для вывода, изменения и удаления ответа"""

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsOwner | IsAdmin,)


# __________________TestTry________________________


class TestTryListAPIView(ListAPIView):
    """Отображение для вывода списка попыток сдачи теста"""

    queryset = TestTry.objects.all()
    serializer_class = TestTrySerializer
    permission_classes = (IsOwner | IsAdmin,)


class TestTryAPIView(RetrieveUpdateDestroyAPIView):
    """Отображение для вывода, изменения и удаления списка ответов"""

    queryset = TestTry.objects.all()
    serializer_class = TestTrySerializer
    permission_classes = (IsOwner | IsAdmin,)


class QuizAPIView(APIView):
    """Отображение для вывода и прохождения теста"""

    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def get(self, request, **kwargs):
        """Выводит тест с вопросами и вариантами ответов для прохождения"""

        user = self.request.user
        test_item = get_object_or_404(Test, pk=kwargs["pk"])
        test_try, _ = TestTry.objects.get_or_create(
            linked_user=user, linked_test=test_item
        )
        serializer = QuizSerializer(test_item)

        response = serializer.data

        return Response(response, status.HTTP_201_CREATED)

    def post(self, request, pk):
        """Принимает ответы пользователя и выводит результаты теста"""

        user = self.request.user
        user_answer = request.data.get("answers")
        test_item = get_object_or_404(Test, pk=pk)
        questions = Question.objects.filter(linked_test=test_item)
        test_try, _ = TestTry.objects.get_or_create(
            linked_user=user, linked_test=test_item
        )
        points_to_pass = test_item.points_to_success
        questions_with_wrong_answer = []

        for answer_id, question in enumerate(questions):
            answer = (
                Answer.objects.filter(linked_question=question)
                .filter(is_true=True)
                .first()
                .number
            )
            scores = question.points_per_answer
            question_with_wrong_answer = check_answers(
                question=question,
                user_answer=user_answer[answer_id],
                right_answer=answer,
                scores=scores,
                test_try=test_try,
            )
            if question_with_wrong_answer:
                questions_with_wrong_answer.append(question_with_wrong_answer)

        points = test_try.points_quantity

        check_test_pass(points=points, points_to_pass=points_to_pass, test_try=test_try)

        if test_try.is_passed:
            response = {
                "result": "Тест успешно пройдет. Поздравляю!",
                "right_answers": f"Отвечено на {test_try.right_answers_quantity} из {test_item.questions_quantity}",
                "scores": f"Набрано {test_try.points_quantity} очков.",
            }
        else:
            response = {
                "results": "К сожалению тест не пройден",
                "wrong_answers_quantity": f"Вы ответили неправильно на {test_item.questions_quantity - test_try.right_answers_quantity} вопросов",
                "wrong_answers": f"Не отвеченные вопросы {questions_with_wrong_answer}",
            }
        return Response(response, status.HTTP_200_OK)

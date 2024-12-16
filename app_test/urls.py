from django.urls import path

from app_test.apps import AppTestConfig
from app_test.views import (
    QuizAPIView,
    TestCreateAPIView,
    TestListAPIView,
    TestAPIView,
    QuestionCreateAPIView,
    QuestionListAPIView,
    QuestionAPIView,
    AnswerListAPIView,
    AnswerCreateAPIView,
    AnswerAPIView,
    TestTryListAPIView,
    TestTryAPIView,
)

app_name = AppTestConfig.name

urlpatterns = [
    path("create/", TestCreateAPIView.as_view(), name="test-create"),
    path("list/", TestListAPIView.as_view(), name="test-list"),
    path("<int:pk>/", TestAPIView.as_view(), name="test-detail"),
    path("question/create/", QuestionCreateAPIView.as_view(), name="question-create"),
    path("question/list/", QuestionListAPIView.as_view(), name="question-list"),
    path("question/<int:pk>/", QuestionAPIView.as_view(), name="question-detail"),
    path("answer/create/", AnswerCreateAPIView.as_view(), name="answer-create"),
    path("answer/list/", AnswerListAPIView.as_view(), name="answer-list"),
    path("answer/<int:pk>/", AnswerAPIView.as_view(), name="answer-detail"),
    path("quiz/<int:pk>/", QuizAPIView.as_view(), name="quiz"),
    path("test_try/list/", TestTryListAPIView.as_view(), name="test-try-list"),
    path("test_try/<int:pk>/", TestTryAPIView.as_view(), name="test-try-detail"),
]

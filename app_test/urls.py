from django.urls import path

from app_test.apps import AppTestConfig
from app_test.views import TestCreateAPIView, TestListAPIView, TestRetrieveAPIView, TestUpdateAPIView, \
    TestDestroyAPIView, QuestionCreateAPIView, QuestionListAPIView, QuestionRetrieveAPIView, QuestionUpdateAPIView, \
    QuestionDestroyAPIView, AnswerListAPIView, AnswerCreateAPIView, AnswerRetrieveAPIView, AnswerUpdateAPIView, \
    AnswerDestroyAPIView

app_name = AppTestConfig.name

urlpatterns = [
    path('create/', TestCreateAPIView.as_view(), name='test-create'),
    path('list/', TestListAPIView.as_view(), name='test-list'),
    path('<int:pk>/', TestRetrieveAPIView.as_view(), name='test-retrieve'),
    path('update/<int:pk>/', TestUpdateAPIView.as_view(), name='test-update'),
    path('delete/<int:pk>/', TestDestroyAPIView.as_view(), name='test-delete'),

    path('question/create/', QuestionCreateAPIView.as_view(), name='question-create'),
    path('question/list/', QuestionListAPIView.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionRetrieveAPIView.as_view(), name='question-retrieve'),
    path('question/update/<int:pk>/', QuestionUpdateAPIView.as_view(), name='question-update'),
    path('question/delete/<int:pk>/', QuestionDestroyAPIView.as_view(), name='question-delete'),

    path('answer/create/', AnswerCreateAPIView.as_view(), name='answer-create'),
    path('answer/list/', AnswerListAPIView.as_view(), name='answer-list'),
    path('answer/<int:pk>/', AnswerRetrieveAPIView.as_view(), name='answer-retrieve'),
    path('answer/update/<int:pk>/', AnswerUpdateAPIView.as_view(), name='answer-update'),
    path('answer/delete/<int:pk>/', AnswerDestroyAPIView.as_view(), name='answer-delete'),
]

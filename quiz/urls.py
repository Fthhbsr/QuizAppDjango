from django.urls import path
from .views import (
    CategoryList,
    QuestionList,
    QuizList
)

urlpatterns = [
    path('', CategoryList.as_view()),
    path('quiz/', QuizList.as_view()),
    path('question/', QuestionList.as_view()),
]
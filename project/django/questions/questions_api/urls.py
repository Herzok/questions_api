from django.urls import path
from .views import *

app_name = 'questions'

urlpatterns = [
    path('', QuestionsListApiView.as_view()),
    path('create', QuestionsCreateApiView.as_view()),
    path('<int:id>', AnswersOfQListApiView.as_view()),
    path('<int:id>/delete', QuestionsDeleteApiView.as_view()),
    path('<int:id>/answers/create', AnswerCreateApiView.as_view()),
    path('answers/<int:id>', AnswerRDApiView.as_view())
]
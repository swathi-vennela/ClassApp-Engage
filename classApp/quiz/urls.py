from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'quiz'

urlpatterns = [
    path('create-quiz/', views.create_quiz, name='create-quiz'),
    path('quiz-home/', views.quiz_home, name='quiz-home'),
    path('quiz/<quiz_id>', views.quiz_detail, name='quiz-detail'),
    path('add-ques/<quiz_id>', views.add_question, name='add-question'),
    path('attempt-quiz/<quiz_id>', views.attempt_quiz, name='attempt-quiz'),
    # path('view-result/<quiz_id>', views.attempt_quiz, name='view-result'),
]

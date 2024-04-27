from django.urls import path, include
from .views import *


urlpatterns = [
    path('questions/', QuestionsView.as_view()),
    path('answers/', AnswersView.as_view()),
    path('courses/', CoursesView.as_view()),
]
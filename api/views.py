from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import *


class QuestionsView(generics.ListAPIView):
    queryset = Question.objects.filter(is_active=True)
    serializer_class = QuestionSerializer

class AnswersView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CoursesView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
from dataclasses import fields
from rest_framework import serializers
from .models import *

class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ('tg_id', 'first_name', 'last_name')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text')

class AnswerSerializer(serializers.ModelSerializer):
    user = TgUserSerializer(read_only=True, many=False)
    course = CourseSerializer(read_only=True, many=False)
    question = QuestionSerializer(read_only=True, many=False)

    class Meta:
        model = Answer
        fields = ('id', 'user', 'course', 'question', 'text', 'is_relevant', 'object', 'is_positive')


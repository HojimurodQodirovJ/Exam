from rest_framework import generics
from .models import Subject, Exam, Question, Test
from .serializers import SubjectSerializer, ExamSerializer, QuestionSerializer, TestSerializer


class SubjectViewSet(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ExamViewSet(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class QuestionViewSet(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestViewSet(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

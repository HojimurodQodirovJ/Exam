from django.urls import path
from .views import SubjectViewSet, ExamViewSet, QuestionViewSet, TestViewSet

urlpatterns = [
    path('subject/', SubjectViewSet.as_view(), name='subject_list'),
    path('exam/', ExamViewSet.as_view(), name='exam_list'),
    path('question/', QuestionViewSet.as_view(), name='question_list'),
    path('test/', TestViewSet.as_view(), name='test_list'),
]

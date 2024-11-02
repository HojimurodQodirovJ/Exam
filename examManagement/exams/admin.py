from django.contrib import admin
from .models import Subject, Exam, Question, Test

admin.site.register([Subject, Exam, Question, Test])

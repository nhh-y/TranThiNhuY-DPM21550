from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, CustomAuthToken, QuestionViewSet, ExamViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'exams', ExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', CustomAuthToken.as_view(), name='api_login'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.question_list, name='question_list'),
]

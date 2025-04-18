from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from quiz.models import *
from quiz.serializers import TeacherSerializer, QuestionSerializer, ExamSerializer
from django.shortcuts import render
from .models import Question 
# import docx
from .gemini import generate_questions_from_text
from .forms import ImportWordForm
from django.shortcuts import render
from .models import Question
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quiz/question_list.html', {'questions': questions})

# Viewset cho Teacher (giáo viên)
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = TeacherSerializer

# API đăng nhập để lấy Token
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})

# Viewset cho Question (câu hỏi)
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Viewset cho Exam (đề kiểm tra)
class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

def import_questions_from_word(request):
    if request.method == 'POST':
        form = ImportWordForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['word_file']
            document = docx.Document(file)

            paragraphs = [p.text.strip() for p in document.paragraphs if p.text.strip()]
            questions = []
            current = {}

            for line in paragraphs:
                if line.lower().startswith("câu"):
                    if current:
                        questions.append(current)
                        current = {}
                    current['question_text'] = line.split(":", 1)[-1].strip()
                elif line.startswith("A."):
                    current['option_a'] = line[2:].strip()
                elif line.startswith("B."):
                    current['option_b'] = line[2:].strip()
                elif line.startswith("C."):
                    current['option_c'] = line[2:].strip()
                elif line.startswith("D."):
                    current['option_d'] = line[2:].strip()
                elif "đáp án" in line.lower():
                    current['correct_answer'] = line.split(":")[-1].strip().upper()

            if current:
                questions.append(current)

            for q in questions:
                if all(k in q for k in ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']):
                    Question.objects.create(
                        question_text=q['question_text'],
                        option_a=q['option_a'],
                        option_b=q['option_b'],
                        option_c=q['option_c'],
                        option_d=q['option_d'],
                        correct_answer=q['correct_answer']
                    )

            return render(request, 'import_success.html')

    else:
        form = ImportWordForm()

    return render(request, 'import_word.html', {'form': form})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quiz/question_list.html', {'questions': questions})

from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class Teacher(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='teacher_groups',  # Đổi related_name thành tên không trùng với auth.User.groups
        blank=True,
        help_text='The groups this teacher belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='teacher_permissions',  # Đổi related_name để tránh xung đột
        blank=True,
        help_text='Specific permissions for this teacher.',
        verbose_name='user permissions',
    )

class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'Trắc nghiệm'),
        ('Essay', 'Tự luận'),
    ]
    content = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    answer = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Exam(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Thời gian làm bài (phút)")
    questions = models.ManyToManyField(Question, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

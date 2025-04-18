from django.contrib import admin
from .models import Question, Exam, Teacher
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "Hệ thống quản lý đề kiểm tra"
admin.site.site_title = "Hệ thống quản lý"
admin.site.index_title = "Trang chủ"

admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Teacher)

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Nhóm người dùng"
        verbose_name_plural = "Quản lý nhóm người dùng"

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Tài khoản"
        verbose_name_plural = "Quản lý tài khoản"
import google.generativeai as genai
genai.configure(api_key="AIzaSyCgE8tZoTw8DrT4z7_GyQ_Yg8kkcPlQjbw")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Tạo 3 câu hỏi trắc nghiệm môn Toán lớp 7 về đại số, mỗi câu có 4 đáp án A, B, C, D và đáp án đúng.")



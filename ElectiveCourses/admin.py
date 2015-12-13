from django.contrib import admin

from .forms import CourseCreateForm
from .forms import TeacherCreateForm
from .forms import StudentCreateForm
from .forms import FeedbackCreateForm

from .models import Course
from .models import Teacher
from .models import Student
from .models import Feedback


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'length', 'teacher']
    ordering = ["name"]
    form = CourseCreateForm


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user_model', 'name', 'surname', 'experience']
    ordering = ["name"]
    form = TeacherCreateForm


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user_model', 'name', 'surname']
    ordering = ["name"]
    form = StudentCreateForm


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'mark', 'comment']
    ordering = ["mark"]
    form = FeedbackCreateForm

admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Feedback, FeedbackAdmin)

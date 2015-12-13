from django import forms
from .models import Course
from .models import Teacher
from .models import Student
from .models import Feedback


class CourseCreateForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'subject', 'length', 'teacher']


class TeacherCreateForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['user_model', 'name', 'surname', 'experience']


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['user_model', 'name', 'surname']


class FeedbackCreateForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['course', 'student', 'mark', 'comment']

from django.db import models
from django.conf import settings


class Teacher(models.Model):
    user_model = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=128, default='Unknown')
    surname = models.CharField(max_length=128, default='Unknown')
    experience = models.IntegerField(default=0)


class Student(models.Model):
    user_model = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=128, default='Unknown')
    surname = models.CharField(max_length=128, default='Unknown')


class Course(models.Model):
    name = models.CharField(max_length=128, default='Unknown')
    subject = models.CharField(max_length=128, default='Unknown')
    length = models.IntegerField(default=5)
    teacher = models.ForeignKey(Teacher, null=True)
    student = models.ManyToManyField(Student)


class Feedback(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    mark = models.IntegerField(default=0)
    comment = models.CharField(max_length=512, default='Teacher did not leave any comments')

from django.shortcuts import render
from .models import Course
from .models import Teacher
from .models import Student
from .models import Feedback
from django import http
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

import logging
logger = logging.getLogger(__name__)


def define_user_type(user):
    tch = Teacher.objects.filter(user_model=user)
    std = Student.objects.filter(user_model=user)

    if tch:
        return 1
    elif std:
        return 2
    else:
        return 0


def index(request):
    try:
        context = {
            'courses': Course.objects.all(),
        }
        if request.user.is_authenticated():
            context = {
                'courses': Course.objects.all(),
                'user': request.user,
                'user_type': define_user_type(request.user),
            }

        return render(request, 'index.html', context)
    except Exception as e:
        logger.error('Problems with rendering index.html: ' + str(e))


def login_action(request):
    try:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return http.HttpResponseRedirect("/profile/")
        else:
            context = {
                'error': 'Username or password are incorrect'
            }
            return render(request, 'error.html', context)
    except Exception as e:
        logger.error('Problems with loging in user: ' + str(e))


def login_view(request):
    try:
        if request.user.is_authenticated():
            return http.HttpResponseRedirect("/profile/")
        return render(request, 'login.html')
    except Exception as e:
        logger.error('Problems with rendering login.html: ' + str(e))


def complete_registration(request):
    return render(request, 'completeRegistration.html')


def complete_registration_action(request):
    try:
        if not request.user.is_authenticated():
            return http.HttpResponseRedirect("/profile/")
        n = request.POST.get('name', '')
        s = request.POST.get('surname', '')
        if request.POST.get('is_teacher', False):
            t = Teacher(user_model=request.user, name=n, surname=s)
            t.save()
        else:
            stud = Student(user_model=request.user, name=n, surname=s)
            stud.save()
        return http.HttpResponseRedirect("/profile/")
    except Exception as e:
        logger.error('Problems with loging in user: ' + str(e))


def profile(request):
    try:
        if request.user.is_authenticated():
            context = {}
            type = define_user_type(request.user)

            if type == 1: #Teacher
                t = Teacher.objects.filter(user_model=request.user).first()
                course = Course.objects.filter(teacher=t).first()
                if course:
                    context = {
                        'course': course,
                        'teacher': t,
                        'students': course.student.all(),
                    }
                else:
                    context = {
                        'teacher': t,
                    }
                return render(request, 'profileTeacher.html', context)
            elif type == 2: #Student
                s = Student.objects.filter(user_model=request.user).first()
                context = {
                    'student': s,
                    'courses': Course.objects.filter(student=s)
                }
                return render(request, 'profileStudent.html', context)
            else:
                return http.HttpResponseRedirect("/complete_registration/")
        else:
            return http.HttpResponseRedirect("/login/")

    except Exception as e:
        logger.error('Problems with entering user profile: ' + str(e))


def add_student_to_course(request):
    try:
        s = Student.objects.filter(user_model=request.user).first()
        c = Course.objects.get(id=request.GET.get("course", None))
        stds = c.student.all()
        if s in stds:
            context = {
                'error': 'You have already entered this course'
            }
            return render(request, 'error.html', context)
        c.student.add(s)
        return http.HttpResponseRedirect("/profile/")
    except Exception as e:
        logger.error('Problems with adding student to course: ' + str(e))


def mark_student(request):
    try:
        s = Student.objects.get(id=request.GET.get("student", None))
        c = Course.objects.get(id=request.GET.get("course", None))

        context = {
            'student': s,
            'course': c,
        }
        return render(request, 'addFeedback.html', context)
    except Exception as e:
        logger.error('Problems with adding a feedback: ' + str(e))


def mark_student_action(request):
    try:
        mk = request.POST.get('mark', '')
        ms = request.POST.get('message', '')
        s = Student.objects.get(id=request.POST.get('student_id', ''))
        c = Course.objects.get(id=request.POST.get('course_id', ''))
        f = Feedback(mark=mk, comment=ms, course=c, student=s)
        f.save()
        return http.HttpResponseRedirect("/course/?course_id=" + request.POST.get('course_id', ''))
    except Exception as e:
        logger.error('Problems with adding a feedback: ' + str(e))


def course(request):
    c = Course.objects.get(id=request.GET.get('course_id', None))
    f = Feedback.objects.filter(course=c)
    context = {
        'course': c,
        'students': c.student.all(),
        'feedbacks': f,
    }
    return render(request, 'course.html', context)


def create_course(request):
    try:
        n = request.POST.get('name', '')
        sb = request.POST.get('subject', '')
        l = request.POST.get('length', '')
        t = Teacher.objects.filter(user_model=request.user).first()
        c = Course(name=n, subject=sb, teacher=t, length=l)
        c.save()
        return http.HttpResponseRedirect("/profile/")
    except Exception as e:
        logger.error('Problems with creating a course: ' + str(e))


def register(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                return http.HttpResponseRedirect("/complete_registration/")
        else:
            return http.HttpResponseRedirect("/register/")
    except Exception as e:
        logger.error('Exception was caught while registration: ' + str(e))


def logout_view(request):
    try:
        logout(request)
        return http.HttpResponseRedirect("/")
    except Exception as e:
            logger.error('PFailed to logout user. Reason: ' + str(e))
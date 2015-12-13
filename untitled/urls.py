"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from ElectiveCourses import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^login_action/$', views.login_action, name='login_action'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^course/$', views.course, name='course'),
    url(r'^create_course/$', views.create_course, name='create_course'),
    url(r'^add_student_to_course/$', views.add_student_to_course, name='add_student_to_course'),
    url(r'^mark_student/$', views.mark_student, name='mark_student'),
    url(r'^mark_student_action/$', views.mark_student_action, name='mark_student_action'),
    url(r'^complete_registration/$', views.complete_registration, name='complete_registration'),
    url(r'^complete_registration_action/$', views.complete_registration_action, name='complete_registration_action'),
    url('^register/', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url='/login/')),
]

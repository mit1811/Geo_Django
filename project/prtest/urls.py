from django.conf.urls import url
from . import views

urlpatterns = [
			url(r'^all/$', views.teacher_list,name='teacher'),
			url(r'^course/$', views.course_list,name='course'),
			url(r'^student/$', views.student_list,name='student'),
			url(r'^(?P<id>\d+)/$', views.link,name='changein'),
			]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Teacher,Student,Course
from django.shortcuts import render,get_object_or_404,redirect

from  django.http import HttpResponse,HttpResponseRedirect
from django.db import connection


def teacher_list(request):
	a=Course.objects.all()
	return render(request,'all.html',{'details':a})

def course_list(request):
	b=Teacher.objects.all()
	return render(request,'course.html',{'details':b})

def student_list(request):
	c=Student.objects.all()
	return render(request,'student.html',{'details':c})

def link(request,id=None):
	source=get_object_or_404(Course,id=id)
	
	# cursor = connection.cursor()
	# cursor.execute("select distinct * from prtest_student join prtest_teacher on prtest_student.students_by_course_id = prtest_teacher.teacher_by_course_id where prtest_student.students_by_course_id="+str(id))
	# items=[{'students':row[1], 'teachers':row[4]} for row in cursor.fetchall()]
	# print (items)
	# return render(request,"change.html",{'items': items})
	q1=Teacher.objects.values('teachers').distinct().filter(teacher_by_course_id=id)
	q2=Student.objects.values('students').distinct().filter(students_by_course_id=id)
	context = {
		"students_name":q1,
		"teachers_name":q2,
		"course":value
	}
	return render(request,'change.html',context)

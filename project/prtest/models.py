# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class Course(models.Model):
	courses=models.CharField(max_length=100,blank=True)

	def __unicode__(self):
		return self.courses

	def get_absolute_url(self):
		return reverse("prtest:changein",kwargs={'id':self.id})

class Teacher(models.Model):
	teachers=models.CharField(max_length=100,blank=True)
	teacher_by_course=models.ManyToOneField(Course,null=True)
	
	def __unicode__(self):
		return self.teachers		

class Student(models.Model):
	students=models.CharField(max_length=100,blank=True)
	students_by_course=models.ForeignKey(Course,null=True)
	
	def __unicode__(self):
		return self.students 		


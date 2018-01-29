# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . models import Value 

def name1(req,s1):
	if (s1=='en'):
		a='english'
		return render(req,"index.html",{'question_text':a})
	elif (s1=='es'):
		a='spanish'
		return render(req,"index.html",{'question_text':a})
	else:
		return render(req,"index.html",{'question_text':s1})		
# Create your views here.

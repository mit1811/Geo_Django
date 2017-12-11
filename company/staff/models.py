# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.
	

class Recuiter(models.Model):
	recuitername=models.CharField(max_length=100)
	manger_by_recuiter=models.ForeignKey(User,null=True)
	search=models.CharField(max_length=100,null=True)

	def __unicode__(self):
		return self.recuitername

	def get_absolute_url(self):
		return reverse("staff:change_by_id",kwargs={'id':self.id})			

class Client(models.Model):
	clientname=models.CharField(max_length=100)

	def __unicode__(self):
		return self.clientname

class Applicant(models.Model):
	applicantname=models.CharField(max_length=100)
	fname=models.CharField(max_length=100,null=True)
	lname=models.CharField(max_length=100,null=True)
	uniname=models.CharField(max_length=100,null=True)
	description=models.TextField(null=True)
	email=models.CharField(max_length=100,null=True)
	languagesknow=models.TextField(null=True)
	contactnumber=models.CharField(max_length=12,null=True)

	def __unicode__(self):
		return self.applicantname





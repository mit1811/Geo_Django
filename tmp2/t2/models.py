# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Value(models.Model):
	question_text=models.CharField(max_length=200)

	def __unicode__(self):
		return self.question_text

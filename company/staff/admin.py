# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Recuiter,Client,Applicant

admin.site.register(Recuiter)
admin.site.register(Client)
admin.site.register(Applicant)
# Register your models here.

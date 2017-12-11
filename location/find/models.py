# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.gis.db import models as gis_models

class Location(models.Model):
	address=models.CharField(max_length=100)
	position=GeopositionField()
	

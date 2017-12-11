# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Location
from .forms import LocationForm

def poi_list(request):
	pois = Location.objects.all()
	form = LocationForm(request.GET)
	if request.method=='GET':
		if form.is_valid():
			form=form.save()
	return render(request, 'poi_list.html', {'pois': pois, 'form':form})




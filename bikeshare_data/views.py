# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Data

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		data = Data.objects
		return render(request, 'index.html', {'data': data})

class AboutPageView(TemplateView):
	template_name = "about.html"

class DataPageView(TemplateView):
	template_name = "data.html"

class AvgDistPageView(TemplateView):
	template_name = "avgdist.html"

class CommutePageView(TemplateView):
	template_name = "commute.html"

class SeasonalPageView(TemplateView):
	template_name = "seasonal.html"
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data(models.Model):
	#image
	image = models.ImageField(upload_to = 'images/')
	#textsummary
	summary = models.CharField(max_length = 200) 
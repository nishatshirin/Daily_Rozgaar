# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class skill(models.Model):
	skill_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.skill_name

class city(models.Model):
    city_name = models.CharField(max_length=100)
    city_file = models.FileField()
    def __str__(self):
		return self.city_name
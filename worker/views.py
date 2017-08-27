# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import skill,city
import rdflib

# Create your views here.
def index(request):
	all_skills = skill.objects.all()
	all_cities = city.objects.all()
	template = loader.get_template('worker/index.html')
	context = {
		'all_skills' : all_skills,
		'all_cities' : all_cities,
	}
	return HttpResponse(template.render(context,request))

def skillList(request):
	all_skills = skill.objects.all()
	html = ''
	for sk in all_skills:
		url = '/worker/skill/'+str(sk.skill_name)+'/'
		html += '<a href="' + url + '">' + sk.skill_name + '</a><br>'
	return HttpResponse(html)

def detail(request,skill_name):
	return HttpResponse("<h2>Details for skill: "+str(skill_name)+"</h2>")

def cityList(request):
	all_cities = city.objects.all()
	template = loader.get_template('worker/cityList.html')
	context = {
		'all_cities' : all_cities,
	}
	return HttpResponse(template.render(context,request))

def cityDetail(request,city_name):
	ct = get_object_or_404(city, city_name=city_name)
	g=rdflib.Graph()
	g.parse(ct.city_file)
	res1 = g.query("""
    PREFIX nit: <http://127.0.0.1:3333/>
    SELECT ?fname ?lname ?skill
    WHERE{
    	?x nit:hasFirstName ?fname.
    	?x nit:hasLastName ?lname.
    	?x nit:hasSkill ?skill
    }
    """)

	template = loader.get_template('worker/cityDetail.html')
	context = {
		'city_name' : city_name,
		'res1' : res1,
	}
	return HttpResponse(template.render(context,request))

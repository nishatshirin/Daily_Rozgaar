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
	template = loader.get_template('worker/skillList.html')
	context = {
		'all_skills' : all_skills,
	}
	return HttpResponse(template.render(context,request))

#changed detail to skill Detail
def skillDetail(request,skill_name):
	sk = get_object_or_404(skill, skill_name=skill_name)
	g=rdflib.Graph()
	g.parse(sk.skill_file)
	res2 = g.query("""
	PREFIX nit: <http://127.0.0.1:3333/>
	SELECT ?fname ?lname ?local ?skill_name ?sub_skill
	WHERE{
	    ?x nit:hasFirstName ?fname.
	    ?x nit:hasLastName ?lname.
	    ?x nit:hasLocality ?local.
	    ?x nit:hasSubSkill ?sub_skill.
	    ?x nit:hasSkill """+"'"+skill_name+"'"+"""
	}
    """)
	
	template = loader.get_template('worker/skillDetail.html')
	context = {
		'skill_name' : skill_name,
		'res2' : res2,
	}
	return HttpResponse(template.render(context,request))

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

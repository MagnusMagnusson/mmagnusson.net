# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, loader
from django.http import HttpResponse
import sys
from django.shortcuts import redirect
from django.http import JsonResponse
from matarast.models import *
import json;

sys.path.insert(0, 'opt/django-env/Core/matarast/scripts/')
sys.path.insert(0, 'matarast/scripts/')
import auth

def validate_login(request):
	if('token' in request.session):
		meta = request.META['HTTP_USER_AGENT']
		member = auth.validate_login(request.session['token'],meta)
		return member
	else:
		return None

def index(request):
	template = loader.get_template('matarast/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def login(request):

	template = loader.get_template("matarast/login.html")
	context = {}

	return HttpResponse(template.render(context, request))

def profile(request):
	member = validate_login(request)
	if(not member):
		return login(request)
	template = loader.get_template("matarast/profile.html")
	context = {"member":member}

	return HttpResponse(template.render(context, request))

def ingredient_new(request):
	member = validate_login(request)
	if(not member):
		return login(request)
	template = loader.get_template("matarast/create/new_ingredient.html")
	languages = Language.objects.all()
	foodClasses = Foodclass.objects.all()
	context = {"member":member,
			"languages":languages,
			"foodclasses":foodClasses}

	return HttpResponse(template.render(context, request))

def ingredient_view(request):
	ing = request.path.split("/")[-1]
	try:
		name = Ingredient_Name.objects.filter(name__unaccent__iexact=ing)

		ingredient = name.ingredient
		context = {}
		context['ingredient'] = ingredient
		context['primaryName'] = name.name
		context['names'] = Ingredient_Name.objects.filter(ingredient = ingredient)
		template = loader.get_template("matarast/view/view_ingredient.html")	
		return HttpResponse(template.render(context, request))
	except Exception as e:		
		return HttpResponse(e)




def api_log_in(request):
	if not request.is_ajax():
		D = {
			'success':False,
			'error': "There was an unexpected error with your request"
		}
		return JsonResponse(D)

	member = validate_login(request)	
	if(member):		
		D = {
			'success':False,
			'error': "You are already logged in"
		}
		return JsonResponse(D)
	pWord = request.POST['password'].encode('utf-8')
	uName = request.POST['user'];
	meta = request.META['HTTP_USER_AGENT']
	access = auth.log_in(uName,pWord,meta);
	if not access[0]:
		D = {
			'success':False,
			'error': "Rangt notendanafn/lykilorð"
			
		}		
		return JsonResponse(D)
	else:
		request.session.cycle_key()
		request.session['logged_in'] = True
		request.session['token'] = access[1]
		request.session.set_expiry(0)
		D = {
			'success':True
		}
		return JsonResponse(D)

def api_ingredient_new(request):
	if not request.is_ajax():
		D = {
			'success':False,
			'error': "There was an unexpected error with your request"
		}
		return JsonResponse(D)

	member = validate_login(request)	
	if(not member):		
		D = {
			'success':False,
			'error': "You must be logged in to do that!"
		}
		return JsonResponse(D)
	try:
		data = json.loads(request.POST['data'])

		desc = data['description']
		img = data['image']
		classList = data['classes']
		ingredient = Ingredient()
		ingredient.description = desc
		ingredient.image=img 
		ingredient.save()
		for lang in data['names']:
			string = data['names'][lang]
			if(string and not string == ""):		
				language = Language.objects.get(short=lang)
				newName = Ingredient_Name()
				newName.language = language
				newName.name = string
				newName.ingredient = ingredient
				newName.save()
		st = set()
		for fc in classList:
			_class = Foodclass.objects.get(id = fc)
			st.add(_class)
			for subClass in _class.subclasses.all():
				st.add(subClass)
		for _class in st:
			ingredient.classes.add(_class)
		ingredient.save()

		d = {'name':newName.name}
		success = True
		error = None
	except Exception as e:
		success = False
		error = e
		d = None
	D = {
		'success':success,
		'error': error,
		'data':d
	}
	return JsonResponse(D)
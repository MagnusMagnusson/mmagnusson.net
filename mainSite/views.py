# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, loader
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def index(request):
	template = loader.get_template('mainSite/index.html')
	context = {}
	return HttpResponse(template.render(context, request))



def about(request):
	template = loader.get_template('mainSite/about.html')
	context = {}
	return HttpResponse(template.render(context, request))


def contact(request):
	template = loader.get_template('mainSite/contact.html')
	context = {}
	return HttpResponse(template.render(context, request))

def favico(request):
	return redirect('../static/mainSite/images/favicon.ico')
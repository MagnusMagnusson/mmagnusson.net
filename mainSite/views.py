# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, loader
from django.http import HttpResponse
# Create your views here.

def index(request,self):
	template = loader.get_template('mainSite/index.html')
	context = {}
	return HttpResponse(template.render(context, request))
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, loader
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
	template = loader.get_template('matarast/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

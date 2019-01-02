# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class Ingredient(models.Model):
	id = models.AutoField(primary_key = True)
	description = models.TextField()

class Language(models.Model):
	name = models.CharField(max_length = 30)
	short = models.CharField(max_length = 3, primary_key = True)

class Ingredient_Name(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	ingredient = models.ForeignKey(Ingredient)
	language = models.ForeignKey(Language)

class Foodclass(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	subclasses = models.ManyToManyField('self')

class Recipy(models.Model):
	id = models.AutoField(primary_key = True)
	description = models.TextField()
	subRecipies = models.ManyToManyField('self')

class Ingredient_Recipy(models.Model):
	id = models.AutoField(primary_key = True)
	quantity = models.DecimalField(decimal_places = 2, max_digits = 5)
	unit = models.CharField(max_length = 10)
	recipy = models.ForeignKey(Recipy)
	ingredient = models.ForeignKey(Ingredient)

class step(models.Model):
	id = models.AutoField(primary_key = True)
	index = models.IntegerField()
	primaryRecipy = models.ForeignKey(Recipy,related_name='recipy')
	description = models.TextField()
	stepRecipy = models.ForeignKey(Recipy,related_name ='proxy', null=True)
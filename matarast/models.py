# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
 
class Foodclass(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	subclasses = models.ManyToManyField('self',symmetrical=False)

class Ingredient(models.Model):
	id = models.AutoField(primary_key = True)
	description = models.TextField()
	image = models.URLField()
	classes = models.ManyToManyField(Foodclass,symmetrical=False)

class Language(models.Model):
	name = models.CharField(max_length = 30)
	short = models.CharField(max_length = 3, primary_key = True)

class Ingredient_Name(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	ingredient = models.ForeignKey(Ingredient)
	language = models.ForeignKey(Language)
	class Meta:
			unique_together = (("name", "language"),)




class recipie(models.Model):
	id = models.AutoField(primary_key = True)
	description = models.TextField()
	subrecipies = models.ManyToManyField('self',related_name = "subrecipie", symmetrical=False)

class recipie_Name(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	ingredient = models.ForeignKey(recipie)
	language = models.ForeignKey(Language)
	class Meta:
			unique_together = (("name", "language"),)

class Ingredient_recipie(models.Model):
	id = models.AutoField(primary_key = True)
	quantity = models.DecimalField(decimal_places = 2, max_digits = 5)
	unit = models.CharField(max_length = 10)
	recipie = models.ForeignKey(recipie)
	ingredient = models.ForeignKey(Ingredient)

class step(models.Model):
	id = models.AutoField(primary_key = True)
	index = models.IntegerField()
	primaryrecipie = models.ForeignKey(recipie,related_name='primaryrecipie')
	description = models.TextField()
	steprecipie = models.ForeignKey(recipie,related_name ='proxy', null=True)



# Memberships

class Member(models.Model):
	id = models.BigIntegerField(primary_key = True)
	name = models.CharField(max_length=20, unique = True)
	salt = models.CharField( max_length=256)
	password = models.CharField(max_length = 256)
	permissions = models.IntegerField()

class Login_log(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(Member)
	time = models.DateTimeField()
	lastRefresh = models.DateTimeField(null = True)
	expires = models.BooleanField(default = True)
	ip = models.CharField(max_length = 50)
	cookie = models.CharField(max_length = 256, unique = True, null = True)


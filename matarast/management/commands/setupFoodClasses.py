from django.core.management.base import BaseCommand, CommandError
from matarast.models import *
import sys
sys.path.insert(0, 'matarast/scripts/')
import auth
import random

class Command(BaseCommand):	
	def handle(self, *args, **options):
		#It is very late, I am very lazy, give me a break for ugly coding
		animal = Foodclass()
		animal.name = "Dýraafurð"
		animal.save()
		mammal = Foodclass()
		mammal.name = "Spendýrakjöt"
		mammal.save()
		mammal.subclasses.add(animal)
		
		milk = Foodclass()
		milk.name = "Mjólkurafurð"
		milk.save()
		milk.subclasses.add(animal)
				
		seafood = Foodclass()
		seafood.name = "Sjávarfang"
		seafood.save()
		seafood.subclasses.add(animal)

		fish = Foodclass()
		fish.name = "Fiskur"
		fish.save()
		fish.subclasses.add(animal)
		fish.subclasses.add(seafood)

		shell = Foodclass()
		shell.name = "Skelfiskur"
		shell.save()
		shell.subclasses.add(animal)
		shell.subclasses.add(seafood)
		
		bird = Foodclass()
		bird.name = "Fuglakjöt"
		bird.save()
		bird.subclasses.add(animal)
				
		egg = Foodclass()
		egg.name = "Egg"
		egg.save()
		egg.subclasses.add(animal)

		wheat = Foodclass()
		wheat.name = "Hveitivara (Glútein)"
		wheat.save()
			
		nut = Foodclass()
		nut.name = "Hnetur"
		nut.save()

		tree = Foodclass()
		tree.name = "Trjáhnetur"
		tree.save()
		tree.subclasses.add(nut)

		peanut = Foodclass()
		peanut.name = "Jarðhnetur"
		peanut.save()
		peanut.subclasses.add(nut)
				
		soy = Foodclass()
		soy.name = "Sojabaunir"
		soy.save()

		sesame = Foodclass()
		sesame.name = "Sesam"
		sesame.save()
				
		fungi = Foodclass()
		fungi.name = "Sveppir"
		fungi.save()

		mold = Foodclass()
		mold.name = "Mygla"
		mold.save()
		mold.add(fungi)

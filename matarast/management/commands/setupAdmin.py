from django.core.management.base import BaseCommand, CommandError
from matarast.models import *
import sys
sys.path.insert(0, 'matarast/scripts/')
import auth
import random

class Command(BaseCommand):	
	def add_arguments(self, parser):
		parser.add_argument('username', nargs='+', type=str)
		parser.add_argument('password', nargs='+', type=str)

	def handle(self, *args, **options):
		uName = options['username'][0]
		pWord = options['password'][0]
		
		admin = Member()
		admin.name = uName
		password = auth.hash_password(pWord,10000)
		admin.password = password[0]
		admin.salt = password[1]
		admin.permissions = 7
		while True:
			id = random.randint(1,9223372036854775806)
			try:
				member = Member.objects.get(id = id)
			except Member.DoesNotExist as ex:
				admin.id = id 
				break
		
		admin.save()

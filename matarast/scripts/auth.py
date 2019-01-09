import hashlib
import sha3
import random 
from matarast.models import Login_log
from matarast.models import Member
import string
import datetime

def hash_password(password, iterations, salt = None):
	if not type(password) == type("String"):
		raise TypeError("Password not a string")

	if(not salt):
		salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(64))

	s = hashlib.sha3_512()

	password = bytes(password.encode('utf-8'))
	salt = bytes(salt.encode('utf-8'))

	for i in range(iterations):
		password += salt
		s.update(password)
		password = s.hexdigest()
	return (password,salt)

def validate_password(password,tuple):
	if not len(tuple)==2:
		raise ValueError("The given hash must have both a password and salt")
	if not type(tuple[0] == type("string")):
		raise TypeError("The given hash and salt must be strings")
	if not type(password) == type("string"):
		raise TypeError("The given password must be string")
	hashed_password = hash_password(password,10000,tuple[1])[0]
	return tuple[0] == hashed_password

def log_in(username,password,meta):
	try:
		member = Member.objects.get(name = username)
	except Member.DoesNotExist as ex:
		return (False,None)
	salt = member.salt
	hash = member.password
	try:
		access = validate_password(password,(hash,salt))
	except ValueError as ex:
		return (False,None)
	except TypeError as ex:
		return (False,None)
	if not access:
		return (False,None)
	else:
		login = Login_log()
		login.user = member
		login.time = datetime.datetime.now()
		while True:		
			cookie = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
			try:
				login = Login_log.objects.get(cookie = cookie)
			except Login_log.DoesNotExist as ex:
				break
		s = hashlib.sha3_512()
		s.update(meta)
		digest = s.hexdigest()[:50]
		login.ip = digest
		login.cookie = cookie
		login.save()
		return (True,cookie)

#Takes in a cookie and metadata and returns the appropriate user if valid
def validate_login(cookie,meta):
	s = hashlib.sha3_512()
	s.update(meta)
	digest = s.hexdigest()[:50]
	try:
		login = Login_log.objects.get(ip = digest, cookie = cookie)
	except Login_log.DoesNotExist as ex:
		return None

	return login.user
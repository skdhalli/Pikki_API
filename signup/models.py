import time
import socket
import django.models as models

# Request classes
class NewUser(models.Model):
	def __init__(self, kw):
		self.username = kw['username']
		self.email = kw['email']
		self.password = kw['password']
	
class NewAccount(models.Model):
	def __init__(self, kw):
		self.ServiceCode = kw['ServiceCode']
		self.Requester = kw['Requester']
		self.User = NewUser(kw['User'])
	
	def Save(self):
		return AccountCreationResponse(None, -1,"Not Implemented yet")

#Response classes
class RegisteredUser(models.Model):
	def __init__(self, _registration_key):
		self.registration_key = _registration_key

class Status(models.Model):
	def __init__(self, _Errno, _Message):
		self.Errno = _Errno
		self.Message = _Message
		self.Timestamp = int(time.time())
		self.Server = socket.gethostbyname(socket.gethostname())

class AccountCreationResponse(models.Model):
	def __init__(self, _registration_key, _Errno, _Message):
		self.User = RegisteredUser(_registration_key)
		self.Status = Status(_Errno, _Message)
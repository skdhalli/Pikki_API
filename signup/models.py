from django.db import models

# Create your models here.
class NewUser(models.Model):
	username = models.CharField(max_length=16, blank=False)
	email = models.TextField(blank=False)
	password = models.TextField(blank=False)
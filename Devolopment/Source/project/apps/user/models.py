# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

choices_sex = (
	(0, 'Nam'),
	(1, 'Nữ'),
)

def directory_path(instance, filename):
	filebase, extension = filename.split('.')
	return '{0}_{1}.{2}'.format(instance.created, instance.id_user, extension)

class User(models.Model):
	id_user = models.CharField(max_length=20, unique=True)
	name = models.CharField(max_length=50)
	sex = models.IntegerField(default=0, choices=choices_sex)
	img = models.ImageField(upload_to=directory_path, default='/images/user.png')
	address = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=15, blank=True)
	mail = models.CharField(max_length=255)
	note = models.TextField(blank=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.id_user

class Role(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	role = models.IntegerField()

	def __str__(self):
		return str(self.user)

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	password = models.CharField(max_length=25)

	def __str__(self):
		return str(self.user)
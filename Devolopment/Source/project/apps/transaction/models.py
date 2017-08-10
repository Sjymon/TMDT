# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from user.models import User
from product.models import Product 

class Transaction(models.Model):
	id_trans = models.CharField(max_length=10, primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	amount = models.FloatField(default=0)
	payment = models.CharField(max_length=20)
	status = models.CharField(max_length=255)
	message = models.TextField()

class Order(models.Model):
	id_order = models.CharField(max_length=10, primary_key=True)
	trans = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	qty = models.FloatField(default=0)
	amount = models.FloatField(default=0)
	status = models.CharField(max_length=255)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from group_product.models import GroupProduct
from unit.models import Unit

# Create your models here.
def directory_path(instance, filename):
	filebase, extension = filename.split('.')
	# instance.id_product_tmp = instance.id_product + 1
	return '{0}_{1}.{2}'.format(instance.name_product, instance.created, extension)

class Product(models.Model):
	id_product = models.AutoField(primary_key=True)
	group = models.ForeignKey(GroupProduct, on_delete=models.CASCADE, related_name='group_product')
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='unit_product')
	name_product = models.CharField(max_length=50, unique=True)
	serial_no = models.IntegerField(default=0)
	# list_img =
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	img = models.ImageField(upload_to=directory_path, blank=True)
	describe = models.TextField(blank=True)
	active = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('product:detailproduct', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('product:editproduct', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('product:deleteproduct', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name_product

	# def save(self, *args, **kwargs):
	# 	if Product.objects.all():
	# 		id_last = Product.objects.all().last().id + 1
	# 	else:
	# 		id_last = 1
	# 	self.id_product = "P" + str(id_last)
	# 	super(Product, self).save(*args, **kwargs)

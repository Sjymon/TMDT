# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class GroupProduct(models.Model):
	id_group = models.AutoField(primary_key=True)
	name_group = models.CharField(max_length=50, unique=True)
	parent_id = models.ForeignKey('self', null=True, blank=True, related_name='children')

	def __str__(self):
		return self.name_group

	def get_all_children(self, include_self=True):
		r = []
		if include_self:
			r.append(self)
		for c in GroupProduct.objects.filter(parent=self):
			_r = c.get_all_children(include_self=True)
			if 0 < len(_r):
				r.extend(_r)
		return r

	def get_absolute_url(self):
		return reverse('group_product:detail', kwargs={'pk': self.pk})

	def get_update_url(self):
		return reverse('group_product:edit', kwargs={'pk': self.pk})

	def get_delete_url(self):
		return reverse('group_product:delete', kwargs={'pk': self.pk})


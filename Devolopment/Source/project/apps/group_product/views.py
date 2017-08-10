# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from group_product.models import GroupProduct
from group_product.forms import GroupProductForm

class ViewGroupProduct(ListView):
	model = GroupProduct
	template_name = 'apps/group_product/group_product.html'

	def get_context_data(self, **kwargs):
		context = super(ViewGroupProduct, self).get_context_data(**kwargs)
		context['group_product_list'] = GroupProduct.objects.all()
		return context

class AddGroupProduct(CreateView):
	model = GroupProduct
	form_class = GroupProductForm
	template_name = 'apps/group_product/add.html'

class DetailGroupProduct(DetailView):
	model = GroupProduct
	template_name = 'apps/group_product/detail.html'

class EditGroupProduct(UpdateView):
	model = GroupProduct
	form_class = GroupProductForm
	template_name = 'apps/group_product/edit.html'

class DeleteGroupProduct(DeleteView):
	model = GroupProduct
	template_name = 'apps/group_product/delete.html'
	success_url = reverse_lazy('group_product:group_product')












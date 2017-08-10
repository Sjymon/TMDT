# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin

from product.models import Product
from product.forms import ProductForm

class ViewProduct(ListView):
	model = Product
	template_name = 'apps/product/product.html'
	def get_context_data(self, **kwargs):
		context = super(ViewProduct, self).get_context_data(**kwargs)
		context['product_list'] = Product.objects.all()
		return context

class AddProduct(CreateView):
	model = Product
	form_class = ProductForm
	template_name = 'apps/product/addproduct.html'	
	# success_message = 'The posts %(post_title)s was created successfully.'

	# def get_success_message(self, cleaned_data):
		# return self.success_message % dict(cleaned_data, post_title=self.object.name)

class DetailProduct(DetailView):
	model = Product
	template_name = 'apps/product/detailproduct.html'
	

class EditProduct(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'apps/product/editproduct.html'	

class DeleteProduct(DeleteView):
	model = Product
	template_name = 'apps/product/deleteproduct.html'
	success_url = reverse_lazy('product:product')
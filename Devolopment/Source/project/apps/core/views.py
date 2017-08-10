# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
	template_name = 'apps/core/index.html'

class AdminView(TemplateView):
	template_name = 'apps/core/main.html'
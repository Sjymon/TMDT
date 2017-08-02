from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
	template_name = 'apps/core/index.html'
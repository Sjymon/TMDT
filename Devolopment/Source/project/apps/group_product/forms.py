from django import forms

from .models import GroupProduct

class GroupProductForm(forms.ModelForm):
	class Meta:
		model = GroupProduct
		fields = [
			'name_group',
			'parent_id',
		]
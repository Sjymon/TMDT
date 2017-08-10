from django import forms

from .models import User, Role, Account

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'id_user',
			

		]
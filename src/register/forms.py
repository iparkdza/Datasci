from django import forms

from .models import register

class regisForm(forms.ModelForm):
	class Meta:
		model = register
		fields = ['username', 'password', 'firstName', 'lastName', 'email', 'birthdate', 'gender']

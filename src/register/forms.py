from django import forms

from .models import register

class regisForm(forms.ModelForm):
	class Meta:
		model = register
		fields = ['username', 'password', 'firstName', 'lastName', 'email', 'birthdate', 'gender']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_username(self): 
		username = self.cleaned_data.get('username')
		return username

	def clean_password(self): 
		password = self.cleaned_data.get('password')
		return password

	def clean_firstName(self): 
		firstName = self.cleaned_data.get('firstName')
		return firstName

	def clean_lastName(self): 
		lastName = self.cleaned_data.get('lastName')
		return lastName

	def clean_birthdate(self): 
		birthdate = self.cleaned_data.get('birthdate')
		return birthdate
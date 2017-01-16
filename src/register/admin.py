from django.contrib import admin

# Register your models here.
from .forms import regisForm
from .models import register

class registerAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "firstName", "lastName", "email", "gender"]
	form = regisForm 
	#class Meta:
	#	model=register
		
admin.site.register(register, registerAdmin)
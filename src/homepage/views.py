from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def home(request):
	
    
    return render(request, "homepage.html", {})

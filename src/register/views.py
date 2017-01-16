from django.shortcuts import render

# Create your views here.
def regis(request):
	return render(request, "regis.html", {})
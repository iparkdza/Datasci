from django.shortcuts import render
from .forms import regisForm
# Create your views here.
def regis(request):
	title = "Registation"
	# if request.user.is_authenticated
		#Go to login page
	

	form = regisForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}
	
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()	
			context = {
				"title": "Thank you",
			}
	
	return render(request, "regis.html", context)
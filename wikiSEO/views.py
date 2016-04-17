from django.shortcuts import render

# Create your views here.

def about(request):
	page_name = "About"
	context = {
		'page_name': page_name,
	}
	return render(request, "about.html", context)
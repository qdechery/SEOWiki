from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from wikiChery.models import Page
from django.core.exceptions import ObjectDoesNotExist
from .forms import ContactForm, PageForm
# Create your views here.

def home(request):
	page_name = 'SEO Wiki'
	form = PageForm(request.POST or None)

	context = {
		"page_name": page_name,
		"form": form,
	}

	
	if form.is_valid():
		instance = form.save(commit=False)
		# if not instance.content:
			# instance.content = 'Q'
		instance.save()
		context = {
			"page_name": "Thank you"
		}

	if request.user.is_authenticated() and request.user.is_staff:
		context = {
			"queryset": [123, 456]
		}

	return render(request, "home.html", context)


def contact(request):
	page_name = 'Contact Us'
	page_name_align_center = True
	context = {
		"page_name": page_name,
		"form": form,
		"page_name_align_center": page_name_align_center,
		# "form.email": "",
	}
	form = ContactForm(request.POST or None)
	# form_email = form.get("email")
	if form.is_valid():
		# for key in form.cleaned_data:
			# print(key, ":", form.cleaned_data.get(key))

		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print(email, message, full_name)
		subject = 'SEO Wiki Contact - Request'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'ofchery@gmail.com']
		contact_message = "%s: %s via %s" %(
			form_full_name, 
			form_message, 
			form_email)

		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				fail_silently=False)

	return render(request, 'forms.html', context)

# def save_page(request):
# 	return HttpResonse("Hello, Save World!")

# def edit_page(request):
# 	return HttpResonse("Hello, Edit World!")

def profile(request):
	page_name = 'Profile'

	context = {
		"page_name": page_name,
	}
	return render(request, 'profile.html', context)
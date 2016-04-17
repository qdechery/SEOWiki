from django import forms
from .models import Page


class ContactForm(forms.Form):
	full_name = forms.CharField(max_length=50, required=False)
	email = forms.EmailField()
	message = forms.CharField(max_length=5000)


class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		fields = ['name', 'content']

	# def clean_name(self):
		# name = self.cleaned_data.get('name')
		# return name
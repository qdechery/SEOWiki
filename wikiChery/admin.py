from django.contrib import admin

from .forms import PageForm
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ["__str__", "content", "updated_at", "created_at",]
	form = PageForm
	# class Meta:
		# model = Page

admin.site.register(Page, PageAdmin)
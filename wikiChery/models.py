from django.db import models

# Create your models here.

class Page(models.Model):
	name = models.CharField(max_length=20, primary_key=True, unique=True)
	content = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __str__(self):
		return self.name



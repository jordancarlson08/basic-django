from django.db import models

class User(models.Model):
	first_name = models.TextField(blank=True, null=True)
	last_name = models.TextField(blank=True, null=True)
	email = models.TextField(blank=True, null=True)

class FileUpload(models.Model):
	new_name = models.TextField(blank=True, null=True)
	original_name = models.TextField(blank=True, null=True)
	full_path = models.TextField(blank=True, null=True)
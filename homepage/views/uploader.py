from django.conf import settings
from django.http import HttpResponse
from django import forms
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
import os.path
from homepage.models import *

LOCAL_PATH = 'c:/Users/Jordan/Desktop'

@view_function
def process_request(request):
	template_vars = {}

	form = UploaderForm()
	if request.method == "POST":
		form = UploaderForm(request.POST)
		if form.is_valid():

			f = FileUpload()
			f.new_name = form.cleaned_data['new_name']
			f.original_name = form.cleaned_data['original_name']
			f.full_path = form.cleaned_data['upload_fullname']
			f.save()

			# files = FileUpload.objects.all()
			# for f in files:
			# 	print('-----------------------')
			# 	print(f.new_name)
			# 	print(f.original_name)
			# 	print(f.full_path)
			# 	print('-----------------------')

			form = UploaderForm()

	template_vars['form'] = form
	return dmp_render_to_response(request, 'uploader.html', template_vars)


class UploaderForm(forms.Form):
	new_name = forms.CharField()
	original_name = forms.CharField(widget=forms.HiddenInput)
	upload_fullname = forms.CharField(widget=forms.HiddenInput) # widget=forms.HiddenInput)
	upload_file =  forms.FileField(required=False, widget=forms.FileInput)


@view_function
def upload(request):

	# fullname = os.path.join('/tmp/uploaded_files', request.FILES['uploadfile'].name)
	fullname = os.path.join(LOCAL_PATH, request.FILES['uploadfile'].name)
	upload = request.FILES['uploadfile']

	with open(fullname, 'wb+') as destination:
		for chunk in upload.chunks():
			destination.write(chunk)

	return HttpResponse(fullname)
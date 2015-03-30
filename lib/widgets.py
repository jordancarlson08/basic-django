from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class AjaxUploadWidget(django.forms.FileField):
	template_name = 'uploader.html'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        context = {
            'url': '/'
        }
        return mark_safe(render_to_string(self.template_name, context))
from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from homepage.models import *
from lib.tables import Table


@view_function
def process_request(request):
	template_vars = {}

	template_vars['initial_page'] = 0

	return dmp_render_to_response(request, 'table.html', template_vars)


@view_function
def get_table(request):
	template_vars = {}

	user_table = UserTable(User.objects.all())
	user_table.paginate(request)

	for user in user_table.qry:
		user_table.append([
			user.first_name,
			user.last_name,
			user.email,
			])

	template_vars['user_table'] = user_table

	return dmp_render_to_response(request, 'table.get_table.html', template_vars)


class UserTable(Table):
	headings = ['First Name', 'Last Name', 'Email']
	endpoint = '/homepage/table.get_table/0/'
	rows_per_page = 5
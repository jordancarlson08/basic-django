#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'jcarlso2.settings'
import django
django.setup()

# import models and run django/python commands
from homepage.models import *

for i in range(100):
	u = User()
	u.first_name = 'fn{}'.format(i)
	u.last_name = 'ln{}'.format(i)
	u.email = '{}{}@example.com'.format(u.first_name, u.last_name)
	u.save()


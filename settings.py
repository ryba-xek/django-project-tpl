# Django settings entry point
# imports all from config/production if server's hostname is in PRODUCTION_HOSTS
# else imports all from config/develop
#
# Please replace all 'changeme' in this and other config files!

from os.path import join, dirname, abspath
import os, sys, socket

#devel or production?
PRODUCTION_HOSTS = ['changeme']
PRODUCTION_ENV = socket.gethostname() in PRODUCTION_HOSTS


#setup paths
PROJECT_ROOT = abspath(dirname(__file__))
CONFIG_ROOT = 'config/production' if PRODUCTION_ENV else 'config/develop'
CONFIG_MODULE_NAME = 'config.%s' % ('production' if PRODUCTION_ENV else 'develop', )
apps_path = join(PROJECT_ROOT, 'apps')
if apps_path not in sys.path:
	sys.path.append(apps_path)


#import all from config folder
for filename in os.listdir(CONFIG_ROOT):
	filename = os.path.splitext(filename)[0]
	if filename.startswith('_'):
		continue

	module_name = '%s.%s' % (CONFIG_MODULE_NAME, filename)
	try:
		config_module = __import__(module_name, globals(), locals(), [])
		for setting in dir(config_module):
			if not setting.startswith('_') and setting == setting.upper():
				locals()[setting] = getattr(config_module, setting)

	except ImportError:
		exit('%s import error' % module_name)


SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zjade7k_4)eje5u!!#!u$4-(%q!9yx0$*w4g752mra5ni=6ant'

ROOT_URLCONF = 'urls'

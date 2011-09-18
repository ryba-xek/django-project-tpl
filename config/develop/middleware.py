# -*- coding: utf8 -*-

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

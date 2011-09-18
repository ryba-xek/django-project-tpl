# -*- coding: utf8 -*-

INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
	#'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
	#'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
	'HIDE_DJANGO_SQL': False,
	'SHOW_TEMPLATE_CONTEXT': True,
	#'TAG': 'div',
}

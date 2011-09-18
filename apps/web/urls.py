# -*- coding: utf8 -*-

from django.conf.urls.defaults import *


urlpatterns = patterns('apps.web.controllers',
	url(r'^$', 'index.index'),
)
#
#urlpatterns += patterns('django.contrib.auth.views',
#	url(r'^login/$', 'login', {'template_name': 'login.tpl', }),
#	url(r'^logout/$', 'logout', {'template_name': 'logged_out.tpl'}),
#)
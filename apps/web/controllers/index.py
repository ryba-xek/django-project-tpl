# -*- coding: utf8 -*-

import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage


#@login_required
def index(request):

	vars = {
	}

	return render_to_response('index.tpl', vars, context_instance=RequestContext(request))


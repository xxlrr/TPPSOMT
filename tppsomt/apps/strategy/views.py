# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


@login_required(login_url="/login/")
def constant(request):
    context = {}
    html_template = loader.get_template('strategy/constant.html')
    return HttpResponse(html_template.render(context, request))

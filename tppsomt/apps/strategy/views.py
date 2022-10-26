# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def constant(request):
    return render(request, "strategy/constant.html", {})


@login_required(login_url="/login/")
def rider(request):
    return render(request, "strategy/rider.html", {})
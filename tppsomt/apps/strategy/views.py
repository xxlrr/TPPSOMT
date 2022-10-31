# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from .models import Constant, Rider


@login_required(login_url="/login/")
def constant(request):
    return render(request, "strategy/constant.html", {})

@login_required(login_url="/login/")
def list_constant(request):
    names = Constant.objects.filter(owner=request.user).values_list('name', flat=True)
    data = {
        'names': list(names)
    }
    return JsonResponse(data)

@login_required(login_url="/login/")
def save_constant(request):
    form = request.POST.dict()
    form.pop('csrfmiddlewaretoken', None)
    id = form.pop('id')
    if not id:
        Constant.objects.create(owner=request.user, **form)
    else:
        Constant.objects.filter(id=id).update(**form)
    return JsonResponse({})

@login_required(login_url="/login/")
def del_constant(request):
    name = request.POST.get('name')
    Constant.objects.filter(owner=request.user, name=name).delete()
    return JsonResponse({})

@login_required(login_url="/login/")
def sel_constant(request):
    name = request.POST.get('name')
    detail = Constant.objects.get(owner=request.user, name=name)
    return JsonResponse(model_to_dict(detail))


@login_required(login_url="/login/")
def rider(request):
    return render(request, "strategy/rider.html", {})

@login_required(login_url="/login/")
def list_rider(request):
    riders = Rider.objects.filter(owner=request.user).values('id', 'profile')
    return JsonResponse({'riders': list(riders)})

@login_required(login_url="/login/")
def save_rider(request):
    form = request.POST.dict()
    form.pop('csrfmiddlewaretoken', None)
    id = form.pop('id')
    if not id:
        Rider.objects.create(owner=request.user, **form)
    else:
        Rider.objects.filter(id=id).update(**form)
    return JsonResponse({})

@login_required(login_url="/login/")
def del_rider(request):
    id = request.POST.get('id')
    Rider.objects.filter(pk=id).delete()
    return JsonResponse({})

@login_required(login_url="/login/")
def sel_rider(request):
    id = request.POST.get('id')
    detail = Rider.objects.get(pk=id)
    return JsonResponse(model_to_dict(detail))


@login_required(login_url="/login/")
def strategy(request):
    return render(request, "strategy/strategy.html", {})


@login_required(login_url="/login/")
def result(request):
    return render(request, "strategy/result.html", {})

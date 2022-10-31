# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from .models import Constant, Rider, Strategy, Result


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
def strategy(request, id=None):
    if request.method == "GET":
        rider_list = Rider.objects.filter(owner=request.user).values('id', 'profile')
        strategy_list = Strategy.objects.filter(owner=request.user).values('id', 'name')
        constant_list = Constant.objects.filter(owner=request.user).values('id', 'name')
        strategy = Strategy.objects.get(pk=id, owner=request.user) if id else {}
        context = {
            "rider_list": rider_list,
            "strategy_list": strategy_list,
            "constant_list": constant_list,
            "strategy": strategy,
        }
        return render(request, "strategy/strategy.html", context=context)
    elif request.method == "POST":
        form = request.POST.dict()
        form.pop('csrfmiddlewaretoken')
        form = {k: v or None for k, v in form.items()}
        action = form.pop('action')
        if action == 'save':
            foreign = {}
            for k, M in Strategy.foreign_fields.items():
                foreign_id = form.pop(k)
                foreign[k] = (M.objects.get(pk=foreign_id) if foreign_id else None)
            if id:
                Strategy.objects.filter(pk=id, owner=request.user).update(**form, **foreign)
                strategy = Strategy.objects.get(pk=id)
            else:
                strategy = Strategy.objects.create(owner=request.user, **form, **foreign)
            strategy.calculate()
            return redirect(reverse('strategy:result', kwargs={'result_id':strategy.result.pk}))
        elif action == 'delete' and id:
            Strategy.objects.filter(pk=id, owner=request.user).delete()
        return redirect(reverse('strategy:strategy'))


@login_required(login_url="/login/")
def result(request, result_id):
    result = Result.objects.get(pk=result_id)
    context = {
        "total_time": result.total_time,
        "time_chart": result.time_chart,
    }
    return render(request, "strategy/result.html", context=context)

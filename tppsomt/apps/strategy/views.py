# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from .models import Constant, Rider, Strategy, Result


@login_required(login_url="/login/")
def constant(request, id=None):
    if request.method == "GET":
        constant_list = Constant.objects.filter(owner=request.user).values('id', 'name')
        constant = Constant.objects.get(pk=id, owner=request.user) if id else {}
        context = {
            "constant_list": constant_list,
            "constant": constant,
        }
        return render(request, "strategy/constant.html", context=context)
    elif request.method == "POST":
        form = request.POST.dict()
        form.pop('csrfmiddlewaretoken')
        form = {k: v or None for k, v in form.items()}
        action = form.pop('action')
        if action == 'save':
            if id:
                Constant.objects.filter(pk=id, owner=request.user).update(**form)
            else:
                Constant.objects.create(owner=request.user, **form)
        elif action == 'delete' and id:
            Constant.objects.filter(pk=id, owner=request.user).delete()
        return redirect(reverse('strategy:constant'))


@login_required(login_url="/login/")
def rider(request, id=None):
    if request.method == "GET":
        rider_list = Rider.objects.filter(owner=request.user).values('id', 'profile')
        rider = Rider.objects.get(pk=id, owner=request.user) if id else {}
        context = {
            "rider_list": rider_list,
            "rider": rider,
        }
        return render(request, "strategy/rider.html", context=context)
    elif request.method == "POST":
        form = request.POST.dict()
        form.pop('csrfmiddlewaretoken')
        form = {k: v or None for k, v in form.items()}
        action = form.pop('action')
        if action == 'save':
            if id:
                Rider.objects.filter(pk=id, owner=request.user).update(**form)
            else:
                Rider.objects.create(owner=request.user, **form)
        elif action == 'delete' and id:
            Rider.objects.filter(pk=id, owner=request.user).delete()
        return redirect(reverse('strategy:rider'))


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

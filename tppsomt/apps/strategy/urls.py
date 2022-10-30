# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.strategy import views


app_name = 'strategy'
urlpatterns = [

    path('constant/', views.constant, name='constant'),
    path('constant/list/', views.list_constant, name='constant_list'),
    path('constant/save/', views.save_constant, name='constant_save'),
    path('constant/del/', views.del_constant, name='constant_del'),
    path('constant/sel/', views.sel_constant, name='constant_sel'),

    path('rider/', views.rider, name='rider'),
    path('strategy/', views.strategy, name='strategy'),
    path('result/', views.result, name='result'),

]

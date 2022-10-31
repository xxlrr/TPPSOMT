# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from . import views


app_name = 'strategy'
urlpatterns = [

    path('constant/', views.constant, name='constant'),
    path('constant/<int:id>/', views.constant, name='constant'),
    path('rider/', views.rider, name='rider'),
    path('rider/<int:id>/', views.rider, name='rider'),
    path('strategy/', views.strategy, name='strategy'),
    path('strategy/<int:id>/', views.strategy, name='strategy'),
    path('result/<int:result_id>/', views.result, name='result'),

]

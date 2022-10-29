# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.strategy import views


app_name = 'strategy'
urlpatterns = [

    path('constant/', views.constant, name='constant'),
    path('rider/', views.rider, name='rider'),
    path('strategy/', views.strategy, name='strategy'),
    path('result/', views.result, name='result'),
    
]

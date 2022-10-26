# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.strategy import views


app_name = 'strategy'
urlpatterns = [

    path('constant/', views.constant, name='constant'),
    path('rider/', views.rider, name='rider'),

    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]

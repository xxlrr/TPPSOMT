# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from apps.strategy.models import Constant, Rider

# Register your models here.
admin.site.register(Constant)
admin.site.register(Rider)
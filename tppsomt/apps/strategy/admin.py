# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Constant, Rider, Strategy, Result

# Register your models here.
admin.site.register(Constant)
admin.site.register(Rider)
admin.site.register(Strategy)
admin.site.register(Result)
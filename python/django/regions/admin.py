# -*- coding: utf-8 -*-

from django.contrib import admin

from models import region, city




class regionAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible',)
    search_fields = ['name']

    class Meta:
        model = region

admin.site.register(region, regionAdmin)


class cityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'visible',)
    search_fields = ['name', 'region__name',]
    class Meta:
        model = city

admin.site.register(city, cityAdmin)

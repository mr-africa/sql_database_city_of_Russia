# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from models import region, city
from russian_cities_and_regions import russian_cities


class Fill_db(View):
    '''
    Fill db all russian cities and regions from file russian_cities_and_regions.py
    This file must be located in current directory.
    If file does not exist, copy it from:
    https://github.com/mr-africa/sql_database_city_of_Russia/tree/master/python/list
    '''
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise Http404
        else:
            for rus_region in russian_cities:
                try:
                    new_region = region.objects.get(name=rus_region)
                except region.DoesNotExist:
                    new_region = region(name=rus_region)
                    new_region.save()
                for item in russian_cities[rus_region]:
                    try:
                        city.objects.get(name=item,
                                         region=new_region)
                    except city.DoesNotExist:
                        new_city = city(name=item,
                                        region=new_region)
                        new_city.save()
            return redirect('/admin/regions/')

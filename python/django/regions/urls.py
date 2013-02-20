# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from views import Fill_db

urlpatterns = patterns('',
                       url(r'^admin/regions/fill_db/$',
                           Fill_db.as_view()),
                       )

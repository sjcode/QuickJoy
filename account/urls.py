#!/usr/bin/python
__author__ = 'sujian'
# -*- coding: UTF-8 -*-

from django.conf.urls import *
from account import views
urlpatterns = patterns('',
                      url(r'^users/$', views.UserList.as_view()),
                      url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
                      )
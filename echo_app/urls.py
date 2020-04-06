# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 10:58
# @Author  : MLee
# @File    : urls.py
from . import views

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import url

urlpatterns = [
    url('^echo/$', views.echo_handler),
    url('^counter/$', views.count_handler),
]

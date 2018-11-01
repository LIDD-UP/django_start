# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: urls.py
@time: 2018/10/31
"""
from django.conf.urls import url
from booktest import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d)(\d)$',views.detail_page)
]


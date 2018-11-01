# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: sql_shell_test.py
@time: 2018/10/31
"""
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_start.settings")# project_name 项目名称
django.setup()
from datetime import datetime,date
from booktest.models import BookInfo,HeroInfo


# 插入数据的时候
# b = BookInfo()
# b.btitle = '射雕英雄传'
# b.bpub_date = datetime.now()
# b.save()
#
# # 获取数据的时候：
# b = BookInfo.objects.all()
# for i in b:
#     print(i.btitle)
# print(b.btitle)



# b=BookInfo()
# b.btitle='abc'
# # b.bpub_date=date(2017,2,1)
# b.bpub_date=datetime.now()
# b.save()

book = BookInfo.objects.get(id=1)
h=HeroInfo()
h.hname='杨过'
h.hgender=2
h.hcomment='he is a big hero'
h.hbook=book
h.save()
# book = BookInfo.objects.get(id=1)
#
# heros = book.heroinfo_set.all()
# for hero in heros:
#     print(hero.hname)

heros = HeroInfo.objects.filter(hbook_id=1)


for hero in heros:
    print(hero)
    print(hero.hname)


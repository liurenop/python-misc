# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:33:54 2018
从古滕堡网站上下载《罗密欧和朱丽叶》
@author: joshua.liu
"""
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')#反馈response对象
print(res.status_code == requests.codes.ok)#通过response对象的status_code属性，来了解是否对网页请求成功
try:
    res.raise_for_status()
except Exception as exc:
    print('There is a problem: %s' % (exc))
print(res.text[:500])#把《罗密欧和朱丽叶》的前500字符打印出来
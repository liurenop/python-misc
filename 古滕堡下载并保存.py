# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:56:09 2018
从古滕堡网站把《罗密哦与朱丽叶》下载并保存在RomeoAndJuliet.txt
@author: joshua.liu
"""
import requests
res = requests.get('http://gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()    

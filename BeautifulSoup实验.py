# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:37:05 2018

@author: joshua.liu
"""
import requests, bs4
res =requests.get('https://www.jensen-group.com/')
res.raise_for_status()
Soup = bs4.BeautifulSoup(res.text)
print(Soup)

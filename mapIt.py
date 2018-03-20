# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:31:05 2018
mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
@author: joshua.liu
"""
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #从命令行get地址
    address = ' '.join(sys.argv[1:])
else:
    #从剪切板get地址
    address = pyperclip.paste()

webbrowser.open('https://map.baidu.com/' + address)
    

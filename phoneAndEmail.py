# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:53:20 2018
phoneAndEmail.py - finds phone number and email addresses on the clipboard.
@author: joshua.liu
"""
import pyperclip, re

# Create phone regex
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?            #area code
        (\s|-|\.)?                    #separator
        (\d{3})                       #first 3 digits
        (\s|-|\.)?                    #separator
        (\d{4})                       #last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?#extension
        )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+             # username
        @                             # @ symbol
        [a-zA-Z0-9.-]+                #domain name
        (\.[a-zA-Z]{2,4})            #dot-something
        )''',re.VERBOSE)

#Find all matches in the clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])  #join the area code, first 3 digits and the last 4 digits together with '-'
    if groups[8] != '':
        phoneNum += ' extention:' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard.
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email adresses found.')
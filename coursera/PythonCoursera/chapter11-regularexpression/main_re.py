'''
Created on 21/02/2016

@author: Carlos Nascimento
'''

import re


strNumber = 'Expression Regular 20, 10, 40'

number = re.findall('[0-9]+', strNumber)

for num in number:
    print num
    
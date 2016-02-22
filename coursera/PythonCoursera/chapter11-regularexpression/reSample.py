'''
Created on 21/02/2016

@author: Carlos
'''

import re

sum = 0
fhand = open('regex_sum_194815.txt')

for linha in fhand:
    listNumbers = re.findall('[0-9]+', linha)
    for num in listNumbers:
        sum = sum + int(num)

print sum
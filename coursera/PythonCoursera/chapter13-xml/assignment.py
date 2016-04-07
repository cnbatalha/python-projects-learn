'''
Created on 13/03/2016

@author: Carlos
'''

import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_194817.xml'
file = urllib.urlopen(url).read()

print 'Retrieved',len(file),'characters'

xmlFile = ET.fromstring(file)

counts = xmlFile.findall('.//count')

print counts
soma = 0

for cont in counts:
    print cont.text
    soma = soma + int(cont.text)

print 'Count:', len(counts)
print 'Sum:', soma
    

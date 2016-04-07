'''
Created on 04/03/2016

@author: Carlos
'''
import urllib
from BeautifulSoup import *

''' url = "http://python-data.dr-chuck.net/comments_42.html"
'''

url = "http://python-data.dr-chuck.net/comments_194820.html"

html = urllib.urlopen(url).read()

soap = BeautifulSoup(html)

tags = soap('span')
cont = 0
soma = 0

for tag in tags:
    cont = cont + 1
    soma = soma + int(tag.contents[0])
    
print soma
print cont
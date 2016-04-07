'''
Created on 06/03/2016

@author: Carlos
'''

import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/known_by_Chahat.html"

position = 18
repeat = 7
cont = 0

while cont < repeat :
    html = urllib.urlopen(url).read()
    soap = BeautifulSoup(html)

    tags = soap('a')
    
    print tags[position-1].contents[0]
    url = tags[position-1].get('href',None)
    print url
    
    cont = cont + 1

    
'''
Created on 06/04/2016

@author: Carlos
'''

import xml.etree.ElementTree as ET

url = 'C:\\SisCommerce\\NFC-e\\13160405828884000190650150000558779000558777-nfe.xml'
url = 'D:\\SISTEMATIC\\Temp\\Desktop\\13160205828884000190650050000636169000636161.xml'
file = open(url).read()

print 'Retrieved',len(file),'characters'
print file

xmlFile = ET.fromstring(file)

print xmlFile

#nfe = xmlFile.findall('.//vICMS')
#print nfe

counts = xmlFile.findall('.//det')
print counts

soma = 0

for cont in counts:
    print cont.text
    soma = soma + float(cont.text)
    
#total = float(counts[len(counts)-1].text)

#soma = soma - total    

print 'Count:', len(counts)
print 'Sum:', soma
#print 'Total:', total

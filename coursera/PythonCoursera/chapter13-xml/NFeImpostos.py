'''
Created on 06/04/2016

@author: Carlos
'''

import xml.etree.ElementTree as ET

url = 'C:\\SisCommerce\\NFC-e\\13160405828884000190650150000558779000558777-nfe.xml'
url = 'D:\\SISTEMATIC\\Temp\\Desktop\\13160205828884000190650010000128219000128215.xml'
file = open(url).read()

print 'Retrieved',len(file),'characters'
print file

xmlFile = ET.fromstring(file)

print xmlFile

counts = xmlFile.findall('.//det')
print counts

soma = 0
somaProd = 0

for cont in counts:    
    cst = cont.find('.//CST')
    pICMS = cont.find('.//pICMS')
    vICMS = cont.find('.//vICMS')
    vProd = cont.find('.//vProd')
    if ( vICMS != None ):
        somaProd = somaProd + float(vProd.text)
        valorProduto = float(vProd.text)*float(pICMS.text)/100
        print vProd.text, ';', cst.text, ';' , (pICMS.text if pICMS != None else 0) , ';' , (vICMS.text if vICMS != None else 0), ';', valorProduto   
        soma = soma +  float(vICMS.text)            
        
        if ( soma != round(somaProd*18/100,2) ):
            print soma , round(somaProd*18/100,2) 
#total = float(counts[len(counts)-1].text)

#soma = soma - total    

print 'Count:', len(counts)
print 'Sum:', soma
print round(somaProd*18/100,2)
#print 'Total:', total

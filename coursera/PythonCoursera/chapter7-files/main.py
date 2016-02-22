'''
Created on 19/02/2016

@author: Carlos Nascimento
'''

print 'Files'

fhand = open('file.txt')

for linha in fhand:
    print linha
    if linha.startswith('linha'):
        print 'achou'

'''
Created on 23/05/2016

@author: Carlos
'''

import json
import urllib2
from firebase.firebase import FirebaseApplication
import sys

def catequizandos():
    with open('config.json') as data_file:    
        config = json.load(data_file)
    
    print config
    req = urllib2.Request(config['url'] + '/catequizando/page/0/300')
    req.add_header('Authorization', 'Basic ' + config['key'] )
    resp = urllib2.urlopen(req)
    content = resp.read()
    ctq = json.loads(content)    
    print content

    fb = FirebaseApplication(config['urlDatabase'], None)    
    
    for c in ctq['content']:      
        response = fb.post('catequizandos/', c, connection=None)
    
  
def turmas():   
    with open('config.json') as data_file:    
        config = json.load(data_file)
    
    print config
    req = urllib2.Request(config['url']  + '/turma')
    req.add_header('Authorization', 'Basic ' + config['key'])
    resp = urllib2.urlopen(req)
    content = resp.read()
    turmas = json.loads(content)    
    print content

    fb = FirebaseApplication(config['urlDatabase'], None)    
    
    for turma in turmas:      
        response = fb.post('turmas/', turma, connection=None)
        
def catequizando_turma():
    with open('config.json') as data_file:    
        config = json.load(data_file)
    
    print config
    req = urllib2.Request(config['url']  + '/turma')
    req.add_header('Authorization', 'Basic ' + config['key'])
    resp = urllib2.urlopen(req)
    content = resp.read()
    lista = json.loads(content)    

    fb = FirebaseApplication(config['urlDatabase'], None)    
    c = fb.get('catequizandos', '-KLiNSOqJcAC62KDbwwk', connection=None)
    print c 
    
    for t in lista:
        print t
        t['KLiNSOqJcAC62KDbwwk'] = c
        response = fb.post('turmas/', t, connection=None)
        
        
    

def main(args ):
    catequizando_turma()

if __name__ == '__main__': 
    main(sys.argv[0])
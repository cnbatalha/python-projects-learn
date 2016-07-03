'''
Created on 23/05/2016

@author: Carlos
'''

import json
import urllib2
from firebase.firebase import FirebaseApplication
import sys
  
def turmas():   
    with open('config.json') as data_file:    
        config = json.load(data_file)
    
    print config
    req = urllib2.Request(config['url'])
    req.add_header('Authorization', 'Basic ' + config['key'])
    resp = urllib2.urlopen(req)
    content = resp.read()
    turmas = json.loads(content)    
    print content

    fb = FirebaseApplication(config['urlDatabase'], None)    
    
    for turma in turmas:      
        response = fb.post('tumas/', turma, connection=None)

        

def main(args ):
    turmas()

if __name__ == '__main__': 
    main(sys.argv[0])
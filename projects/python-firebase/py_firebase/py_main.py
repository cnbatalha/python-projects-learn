'''
Created on 23/05/2016

@author: Carlos
'''
from firebase.firebase import FirebaseApplication

def main(argv):
    
    cont = 0
    
    fb =  FirebaseApplication('https://py-firebase.firebaseio.com/', None)
    new_user = 'Ozgur Vatansever'
    
    
    response = fb.post('/users', new_user, connection=None, params={'print': 'pretty'}, headers={'X_FANCY_HEADER': 'VERY FANCY'})
    cont = cont + 1
    
    print cont
    print response
    
    responseGet = fb.get('/users', None)
    
    print 'response - get'
    print responseGet   

if __name__ == '__main__':
    main(None)


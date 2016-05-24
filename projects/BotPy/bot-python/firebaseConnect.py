'''
Created on 24/05/2016

@author: Carlos
'''
from firebase.firebase import FirebaseApplication

def post( url, data):
    fb = FirebaseApplication('https://consulta-notas.firebaseio.com/', None)
    
    response = fb.post(url, data, connection=None)
    print response
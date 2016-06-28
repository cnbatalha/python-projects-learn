'''
Created on 20/05/2016

@author: Carlos
'''

import notaConsulta
import time
import sys

def main(args):
    # 35150145242914004518550010004261151690070495
    # 35120145242914004518550010004253651650210179
    # 35150145242914004518550010004229071045878490
    print args
    time.sleep(5)
    notaConsulta.consultaPIN(args)
    
    #notaConsulta.consulta('35120145242914004518550010004253651650210179')
    #time.sleep(10)
    #notaConsulta.consulta('35150145242914004518550010004229071045878490')

if __name__ == '__main__': 
    main(sys.argv[1])


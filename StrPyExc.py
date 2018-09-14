import os
import math
#import re
from io import StringIO
import sys



class StrExc:
    def __init__(self,mark='\*\*'):
        self.mark=mark
            
    def get_str(self,pystring):
        old_stdout=sys.stdout
        try:
            redirected_output=sys.stdout=StringIO()
            exec(pystring)
            return_string=redirected_output.getvalue()
            sys.stdout=old_stdout
            return return_string
        except:
            sys.stdout=old_stdout
            return 'wrong: '+ pystring
    
    def str2floatlist(self,pystring):
        list_tempt=self.get_str(pystring)
        list_tempt=list_tempt[1:-2].split(',')
        list_tempt=[float(f) for f in list_tempt]
        #print (list_tempt,'\n\n\n list:',list_tempt[1:-1].split(','))
        return list_tempt
        
    def str2strlist(self,pystring):
        '''
        used when the list gennerated in py script has string as elements
        '''
        list_tempt=self.get_str(pystring)
        list_tempt=list_tempt[2:-3].split('\', \'')
        #list_tempt=[float(f) for f in list_tempt]
        #print (list_tempt,'\n\n\n list:',list_tempt[1:-1].split(','))
        return list_tempt
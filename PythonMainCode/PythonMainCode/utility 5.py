from datetime import datetime
import invalid_exception as ie
import re

def access_file(file):
    # Write your code here
    f=open(file,"r")
    
    
    return f#None #TODO CHANGE THIS RETURN VALUE


def validate_car_number(car_number):
    # Write your code here
    try:
        ## Fill your code here
       valid=re.search("^(NXF)[0-9]{3}.{3}[a-zA_Z]$",car_number)
       if valid is None:
        raise ie.InvalidCarNumberException("Invalid car number")
       
        return True#pass  #TODO: Remove this statement after writing your code
    except ie.InvalidCarNumberException as e:
        ## Fill your code here
       return e.message
        #pass #TODO: Remove this statement after writing your code
    
    

def convert_date(str_date):
    # Write your code here
    d,m,y=map(int,str_date("/"))
    dt=datetime(y,m,d)
    
    return dt#None  #TODO CHANGE THIS RETURN VALUE

    
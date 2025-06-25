from datetime import datetime
from datetime import date
import exception as ex
import re

def read_file(file):
    # Write your code here
    l=[]
    with open(file,'r') as f:
        f_data= f.read().split("\n") #f_data is astring 
        for i in f_data:
            a= i.split(",")
            dt1= convert_date(a[2])
            dt2= convert_date(a[4])
            diff= (dt1 - dt2).days
            if a[7]=="Approved" and diff<=180:
                l.append(a)
    return l#None #TODO CHANGE THIS RETURN VALUE


def validate_request_id(request_id):
    try:
        # Write your code here
        res= re.search("^(R00)[0-9]$", request_id)
        if res is None:
            raise ex.InvalidRequestIdException("Invalid Request Id")
        return True #TODO CHANGE THIS RETURN VALUE
        
    except ex.InvalidRequestIdException as e:
        # Write your code here
        return e.message#None #TODO CHANGE THIS RETURN VALUE
    
   

# def validate_request_id(request_id):
#     try:
#         if not re.match(r"^R00[0-9]$", request_id):
#             raise ex.InvalidRequestIdException("Invalid Request Id")
#         return True
#     except ex.InvalidRequestIdException as e:
#         return e.message




def convert_date(str_date):
    # Write your code here to conver the string to date
    y,m,d= map(int,str_date.split("-"))
    dt= date(y,m,d)
    
    return dt#None  #TODO CHANGE THIS RETURN VALUE


# def convert_date(str_date):
#     dt = datetime.strptime(str_date, "%Y-%m-%d").date()
#     return dt

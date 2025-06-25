from datetime import date
import exception as ex
import re

def read_file(filename):
    lst=[]
    with open(filename,"r") as f:
        reading=f.read().split("\n")
        for a in reading:
            a=a.split(",")
            dt_req=convert_date(a[2])
            dt_trav=convert_date(a[4])
            diff=(dt_req - dt_travel).days
            if a[7]=="Approved" and diff<=180:
                lst.append(a)
    f.close()
    return lst


def convert_date(str_date):
    y,m,d=map(int,str_date.split("-"))
    dt=date(y,m,d)
    return dt
   

def validate_request_id(request_id):
   try:
        res=re.search(r'',request_id)
        if res is None:
            raise ex.InvalidRequestIdException "Invalid request id"
        return True
    except ex.InvalidRequestIdException as e:
        print e.message




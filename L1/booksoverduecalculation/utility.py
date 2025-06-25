# import necessary modules and packages here
import re
import invalid_bookid_exception as ib
from datetime import datetime, date

def read_file(filename):
    # Write your code here
    records = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                records.append(line)
        return records
    except Exception as e:
        return []

def validate_book_id(book_id):
    try:
        p=re.search("^(LIBRARY/)[0-9]{4}$",book_id)
        if p is None:
            raise ib.InvalidBookIDException("Invalid Book ID")    
        else:
            return True
        
    except ib.InvalidBookIDException as e:
        # Write your code here
        return e.message
        

def convert_date(str_date):
    # Write your code here
    y,m,d=map(int,str_date.split("-"))
    dt=date(y,m,d)
    return dt
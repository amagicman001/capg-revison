# import necessary modules and packeges here
import re
import invalid_exception as ie
from datetime import date


def read_file(file):
    # Write your code here
    with open(file, 'r') as f:
        f_obj = f.read().split("\n")
        record_list = []
        for row in f_obj:
            record_list.append(row)  
     
    return record_list #TODO CHANGE THIS RETURN VALUE


def validate_ticket_id(ticket_id):
    try:
        # Write your code here
        valid=re.search("BOOKMY0[0-9]{2}", ticket_id)
        if valid is None:
            raise ie.InvalidTicketIdException("Invalid Ticket Id")
        else:
            return True #TODO CHANGE THIS RETURN VALUE
    
    except ie.InvalidTicketIdException as e:
        return e.message #TODO CHANGE THIS RETURN VALUE



    
def convert_date(str_date):
    # Write your code here
    y, m, d = map(int, str_date.split("-"))
    dt = date(y, m, d)  
    return dt #TODO CHANGE THIS RETURN VALUE

from datetime import date
import exception as ex
import re


def read_file(filename):
        filtered_records = []
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            # filter records: approved by manager and travel within last 180 days
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                fields = line.split(',')
                # fields indexes as per format
                # 0 - request_id, 7 - manager_approval, 4 - date_of_travel
                manager_approval = fields[7].strip()
                date_of_travel_str = fields[4].strip()
                date_of_travel = Utility.convert_date(date_of_travel_str)
                # Check approval and within 180 days from today
                today = date.today()
                delta = (today - date_of_travel).days
                if manager_approval.lower() == 'approved' and 0 <= delta <= 180:
                    filtered_records.append(line)
        except FileNotFoundError:
            # If file not found, return empty list
            return []
        return filtered_records

def validate_request_id(request_id):
        # Must be at least 4 characters, start with 'R', next two chars '0', last char an integer
        if len(request_id) < 4:
            raise InvalidRequestIdException('Invalid Request Id')
        if request_id[0] != 'R':
            raise InvalidRequestIdException('Invalid Request Id')
        if request_id[1:3] != '00':
            raise InvalidRequestIdException('Invalid Request Id')
        if not request_id[-1].isdigit():
            raise InvalidRequestIdException('Invalid Request Id')
        return True

    
def convert_date(str_date):
        # Converts 'yyyy-mm-dd' string to datetime.date object
        return datetime.strptime(str_date, '%Y-%m-%d').date()
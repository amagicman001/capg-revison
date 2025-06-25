### DO NOT ALTER THE GIVEN TEMPLATE.  FILL THE CODE ONLY IN THE PROVIDED PLACES ALONE
# You can add any number of methods and attributes as you required without changing the given template

import emp_reimbursement as er
import utility
import cx_Oracle

db=""
with open('database.properties') as f:
    lines = [line.strip().split("=") for line in f.readlines() if not line.startswith('#') and line.strip()]
    db = {key.strip(): value.strip() for key, value in lines}
   
#Creating Connection String
conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])



class EmpReimbursementService:
    def __init__(self):
        self.emp_reimbursement_list = []

    def get_emp_reimbursement_details(self, filename):
        records = Utility.read_file(filename)
        self.build_emp_reimbursement_list(records)
        return self.emp_reimbursement_list

    def calculate_reimbursement_costs(self, no_of_days, local_kms_travel, grade):
        # Costs tables
        grade = grade.strip()
        # Grade wise costs per day / km
        cost_data = {
            'Level 01': (10000, 1000, 22, 1500),
            'Level 02': (10000, 1000, 22, 1500),
            'Level 03': (4000, 700, 16, 1000),
            'Level 04': (4000, 700, 16, 1000),
            'Level 05': (2500, 450, 12, 750),
            'Level 06': (2500, 450, 12, 750)
        }
        if grade not in cost_data:
            # If grade not found, treat as zeros
            return [0, 0, 0, 0, 0]

        accom_cost_per_day, dining_cost_per_day, local_travel_per_km, allowances_per_day = cost_data[grade]

        accommodation_cost = accom_cost_per_day * no_of_days
        dining_cost = dining_cost_per_day * no_of_days
        local_travel_cost = local_travel_per_km * local_kms_travel
        allowances = allowances_per_day * no_of_days

        total_reimbursement_cost = accommodation_cost + dining_cost + local_travel_cost + allowances

        return [accommodation_cost, dining_cost, local_travel_cost, allowances, total_reimbursement_cost]

    def build_emp_reimbursement_list(self, records):
        for record in records:
            try:
                fields = record.split(',')
                request_id = fields[0].strip()
                Utility.validate_request_id(request_id)

                employee_code = fields[1].strip()
                date_of_request = Utility.convert_date(fields[2].strip())
                grade = fields[3].strip()
                date_of_travel = Utility.convert_date(fields[4].strip())
                no_of_days_of_stay = int(fields[5].strip())
                local_travel_in_kms = float(fields[6].strip())
                manager_approval = fields[7].strip()

                # Create EmpReimbursement object
                emp = EmpReimbursement(request_id, employee_code, date_of_request, grade,
                                       date_of_travel, no_of_days_of_stay, local_travel_in_kms, manager_approval)

                # Calculate costs
                costs = self.calculate_reimbursement_costs(no_of_days_of_stay, local_travel_in_kms, grade)
                emp.set_accomodation_cost(costs[0])
                emp.set_dining_cost(costs[1])
                emp.set_local_travel_cost(costs[2])
                emp.set_allowances(costs[3])
                emp.set_total_reimbursement_cost(costs[4])

                # Add to list
                self.emp_reimbursement_list.append(emp)

            except InvalidRequestIdException as e:
                # Skip invalid request_id with error message (can log if needed)
                pass
            except Exception as e:
                # Skip any malformed record or error silently
                pass

    def add_reimbursement_details(self, emp_list):
        # Connect to Oracle database using cx_Oracle
        import configparser
        config = configparser.ConfigParser()
        config.read('database.properties')
        dsn = cx_Oracle.makedsn(config['DEFAULT']['host'], int(config['DEFAULT']['port']), service_name=config['DEFAULT']['service_name'])
        conn = None
        cursor = None
        try:
            conn = cx_Oracle.connect(user=config['DEFAULT']['username'], password=config['DEFAULT']['password'], dsn=dsn)
            cursor = conn.cursor()

            insert_query = '''
            INSERT INTO reimbursement(request_id, employee_code, date_of_request, grade, date_of_travel, 
            no_of_days_of_stay, local_travel_in_kms, manager_approval, accomodation_cost, dining_cost, allowances, local_travel_cost, total_reimbursement_cost)
            VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13)
            '''
            for emp in emp_list:
                cursor.execute(insert_query, (
                    emp.get_request_id(),
                    emp.get_employee_code(),
                    emp.get_date_of_request(),
                    emp.get_grade(),
                    emp.get_date_of_travel(),
                    emp.get_no_of_days_of_stay(),
                    emp.get_local_travel_in_kms(),
                    emp.get_manager_approval(),
                    emp.get_accomodation_cost(),
                    emp.get_dining_cost(),
                    emp.get_allowances(),
                    emp.get_local_travel_cost(),
                    emp.get_total_reimbursement_cost()
                ))
            conn.commit()
        except Exception as e:
            pass
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def search_reimbursement_request(self, request_id):
        try:
            conn = cx_Oracle.connect(user=config['DEFAULT']['username'], password=config['DEFAULT']['password'], dsn=dsn)
            cursor = conn.cursor()
            query = '''SELECT request_id, employee_code, date_of_request, grade, date_of_travel,
            no_of_days_of_stay, local_travel_in_kms, manager_approval, accomodation_cost, dining_cost,
            allowances, local_travel_cost, total_reimbursement_cost
            FROM reimbursement WHERE request_id = :rid'''
            cursor.execute(query, rid=request_id)
            row = cursor.fetchone()
            if row:
                emp = EmpReimbursement(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
                emp.set_accomodation_cost(row[8])
                emp.set_dining_cost(row[9])
                emp.set_allowances(row[10])
                emp.set_local_travel_cost(row[11])
                emp.set_total_reimbursement_cost(row[12])
                return emp
            else:
                return None
        except Exception as e:
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update_costs(self, no_days):
        pass


  
    

          
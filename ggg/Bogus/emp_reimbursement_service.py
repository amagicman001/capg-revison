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
        self.__emp_reimbursement_list=[]    
    
    def get_emp_reimbursement_details(self, input_file):
        # Write your code here
        lst=utility.read_file(input_file)
        self.build_emp_reimbursement(lst)
        return self.__emp_reimbursement_list
        

    def calculate_reimbursement_costs(self,no_of_days, local_kms_travel, grade):
        # Write your code here
        ac=0.0
        dc=0.0
        ltc=0.0
        alwc=0.0
        tra=0.0
        if grade=="Level01" or grade="Level02":
            ac=10000.0*float(no_of_days)
        elif
        ........


        lst=[ac,dc,ltc,alwc,tra]
        
        return lst #None  #TODO CHANGE THIS RETURN VALUE

    
    def build_emp_reimbursement_list(self, emp_reimburses_records):
        # Write your code here
        for a in emp_reimburses_records:
            valid=utility.validate_request_id(a[0])
            if valid:
                dt2=utility.convert_date(a[2]) 
                dt4=utility.convert_date(a[4])
                obj=er.EmpReimbursementSystem(a[0],a[1],d2,a[3],d4,a[5],float(a[6]),a[7]) 
                cost=self.calculate_reimbursement_cost(a[5],a[6],a[3])
                obj.set_allowance_cost(cost[0])
                obj.set_dining_cost(cost[1])
                .
                .
                .
                self.emp_reimbursement_list.append(obj)            
        return 
    
    
    def add_reimbursement_details(self, reimburse_list):
        # Write your code here
        try:
            conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
            cursor=conn.cursor()
            sql="INSERT INTO reimbursement(....) VALUES (:1,:2,:3,:4.....)"
            for x in reimburse_list:
                l=[]
                l.append(x.get...())
                l.append(x.get...())
                cursor.execute(sql,l)
                conn.commit()
            conn.close()
            cursor.close()
            return
        except cx_Oracle.Error as err:
            return err
    
        
    def search_reimbursement_request(self, request_id):
	    # Write your code here
        try:
            valid=utility.valdate_request_id(request_id)
            if valid:
                conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
                cursor=conn.cursor()
                sql="SELECT * FROM reimbursement WHERE request_id=:1"
                cursor.execute(sql,request_id)
                x=cursor.fetchone()
                if x is None:
                    return None
                else:
                    obj=er.EmpReimbursementSystem(x[0]..........x[7])
                    obj.set_......(x[8])
                    ....(x[12])
                    return obj
            #return
        except cx_Oracle.Error as err:
            return err
	    #return True #TODO CHANGE THIS RETURN VALUE
	
	
    def update_costs(self,no_days):
	    # Write your code here
        try:
            l_obj=[]
            conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
            cursor=conn.cursor()
            sql="UPDATE reimbursement SET allowance=1.1*allowance,local_travel_cost=1.1*local_travel_cost,total_reimbursement_cost=allowance+dining+.... WHERE no_of_days>:1"
            cursor.execute(sql,no_days)
            conn.commit()
            sql2="SELECT * FROM reimbursement WHERE no_days>:1"
            cursor.execute(sql2,no_days)
            data=cursor.fetchall()
            if data is None:
                return None
            else:
                for x in data:
                    obj=er.empReimbursementSystem(x[0]....x[7])
                    obj.set_(x[8])........(x[12])
                    l_obj.append(obj)
                return l_obj
        except cx_Oracle.Error as err:
            return err
        #return None #TODO CHANGE THIS RETURN VALUE 
	
	

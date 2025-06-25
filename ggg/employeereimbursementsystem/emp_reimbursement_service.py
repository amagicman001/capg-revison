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
        f_data= utility.read_file(input_file)
        self.build_emp_reimbursement_list(f_data)
        return self.__emp_reimbursement_list

    def calculate_reimbursement_costs(self,no_of_days, local_kms_travel, grade):
        # Write your code here
        ac=0.0
        dc=0.0
        ltc=0.0
        alc=0.0
        tc=0.0
        if grade=="Level01" or grade=="Level02":
            ac=10000.0*float(no_of_days)
            dc=1000.0*float(no_of_days)
            ltc=22.0*float(local_kms_travel)
            alc=1500.0*float(no_of_days)
            tc= ac+dc+ltc+alc
        elif grade=="Level03" or grade=="Level04":
            ac=4000.0*float(no_of_days)
            dc=700.0*float(no_of_days)
            ltc=16.0*float(local_kms_travel)
            alc=1000.0*float(no_of_days)
            tc= ac+dc+ltc+alc
        elif grade=="Level05" or grade=="Level06":
            ac=2500.0*float(no_of_days)
            dc=450.0*float(no_of_days)
            ltc=12.0*float(local_kms_travel)
            alc=750.0*float(no_of_days)
            tc= ac+dc+ltc+alc
        c=[ac,dc,ltc,alc, tc]
        return c#None  #TODO CHANGE THIS RETURN VALUE

    
    def build_emp_reimbursement_list(self, emp_reimburses_records):
        # Write your code here
        for a in emp_reimburses_records:
            res= utility.validate_request_id(a[0])
            if res==True:
                dt1= utility.convert_date(a[2])
                dt2= utility.convert_date(a[4])
                obj= er.EmpReimbursement(a[0],a[1],dt1,a[3],dt2,int(a[5]),float(a[6]),a[7])
                cost= self.calculate_reimbursement_costs(a[5],a[6],a[3])
                obj.set_accomodation_cost(cost[0])
                obj.set_dining_cost(cost[1])
                obj.set_local_travel_cost(cost[2])
                obj.set_allowances(cost[3])
                obj.set_total_reimbursement_cost(cost[4])
                self.__emp_reimbursement_list.append(obj)                
        return
    
    
    def add_reimbursement_details(self, reimburse_list):
        # Write your code here
        try:
            conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
            cursor= conn.cursor()
            sql="""INSERT INTO reimbursement(request_id,employee_code,date_of_request,grade,date_of_travel,no_of_days_of_stay,local_travel_in_kms,manager_approval,accomodation_cost,dining_cost,allowances,local_travel_cost,total_reimbursement_cost)
                    VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13)"""
            for i in reimburse_list:
                l=[]
                l.append(i.get_request_id())
                l.append(i.get_employee_code())
                l.append(i.get_date_of_request())
                l.append(i.get_grade())
                l.append(i.get_date_of_travel())
                l.append(i.get_no_of_days_of_stay())
                l.append(i.get_local_travel_in_kms())
                l.append(i.get_manager_approval())
                l.append(i.get_accomodation_cost())
                l.append(i.get_dining_cost())
                l.append(i.get_allowances())
                l.append(i.get_local_travel_cost())
                l.append(i.get_total_reimbursement_cost())
                cursor.execute(sql,l)
                conn.commit()
            cursor.close()
            conn.close()
            return
        except cx_Oracle.Error as err:
            return err
    
        
    def search_reimbursement_request(self, request_id):
	    # Write your code here
        try:
            conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
            cursor= conn.cursor()
            sql="SELECT * FROM reimbursement WHERE request_id=:request_id"
            cursor.execute(sql,[request_id])
            x= cursor.fetchone()
            cursor.close()
            conn.close()
            if x is None:
                return None 
            else:
                obj= er.EmpReimbursement(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
                obj.set_accomodation_cost(x[8])
                obj.set_dining_cost(x[9])
                obj.set_allowances(x[10])
                obj.set_local_travel_cost(x[11])
                obj.set_total_reimbursement_cost(x[12])
                return obj
            #return
        except cx_Oracle.Error as err:
            return err
	    #return True #TODO CHANGE THIS RETURN VALUE
	
	
    def update_costs(self,no_days):
	    # Write your code here
        try:
            conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
            cursor= conn.cursor()
            sql="""UPDATE reimbursement SET allowances=1.1*allowances, local_travel_cost=1.1*local_travel_cost, 
                    total_reimbursement_cost=accomodation_cost+dining_cost+allowances+local_travel_cost
                    WHERE no_of_days_of_stay>:no_days"""
            cursor.execute(sql,[no_days])
            conn.commit()
            sql="SELECT * FROM reimbursement WHERE no_of_days_of_stay>:no_days"
            cursor.execute(sql,[no_days])
            data= cursor.fetchall()
            cursor.close()
            conn.close()
            if data is None:
                return None
            else:
                l_obj=[]
                for x in data:
                    obj= er.EmpReimbursement(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
                    obj.set_accomodation_cost(x[8])
                    obj.set_dining_cost(x[9])
                    obj.set_allowances(x[10])
                    obj.set_local_travel_cost(x[11])
                    obj.set_total_reimbursement_cost(x[12])
                    l_obj.append(obj)
                return l_obj
        except cx_Oracle.Error as err:
            return err
        #return None #TODO CHANGE THIS RETURN VALUE 
	
	

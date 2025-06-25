# Please do not change the skelecton code given here
# You can add any number of methods and attributes as you required without changing the given template
import utility as ut
import car as cr
import cx_Oracle
from datetime import datetime,timedelta


##import necessary modules/packages here

db=" "
with open("database.properties") as f:
    lines= [line.strip().split("=") for line in f.readlines() if not line.startswith("#") and line.strip()]
    db = {key.strip(): value.strip() for key, value in lines}
   
##Creating Connection String
conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
cursor=conn.cursor()

class CarService:
    
    def __init__(self):
        self.__discount_dict={}
    
    
    def read_data(self,file_obj):
        # Write your code here
        f_data= file_obj.read().split("\n")
        for f in f_data:
            a= f.split(",")
            valid= ut.validate_car_number(a[1])
            if valid==True:
                dt= ut.convert_date(a[5])
                c= cr.Car(a[0],a[1],a[2],float(a[3]),int(a[4]),dt)
                c.calculate_total_amount()
                dis=self.add_car_details(c)
                #print(dis,type(dis))
                if c.get_no_of_days()>1:
                    if c.get_no_of_days()<=3:
                        self.__discount_dict[a[0]] = c.get_basic_cost()*float(c.get_no_of_days())*0.02
                    else:
                        self.__discount_dict[a[0]] = c.get_basic_cost()*float(c.get_no_of_days())*0.04
        return ##TODO: RETURN VALUE AS PER THE DESCRIPTION
    
    
    
    def add_car_details(self,car_obj):
        # Write your code
        #try:
        sql="""INSERT INTO Car(rental_id,car_number,customer_name,basic_cost,no_of_days,rental_date,total_amount)
                VALUES(:1,:2,:3,:4,:5,:6,:7)"""
        l=[]
        l.append(car_obj.get_rental_id())
        l.append(car_obj.get_car_number())
        l.append(car_obj.get_customer_name())
        l.append(car_obj.get_basic_cost())
        l.append(car_obj.get_no_of_days())
        l.append(car_obj.get_rental_date())
        l.append(car_obj.get_total_amount())
        cursor.execute(sql,l)
        conn.commit()
        #except cx_Oracle.Error as err:
        #    print(err)
        return ##TODO: RETURN VALUE AS PER THE DESCRIPTION
    
    
    
    
    def find_top3_rentals(self):
        # Write your code
        sql="SELECT * FROM Car"
        car_id= set()
        data= dict()
        cursor.execute(sql)
        db_data= cursor.fetchall()
        for i in db_data:
            if i[1] in car_id:
                data[i[1]]+=1
            else:
                car_id.add(i[1])
                data[i[1]]=1
        dat= {}
        for k,v in data.items():
            dat[v]= k
        so= dict(sorted(dat.items(),reverse=True))
        soon= dict()
        i=0
        last=0
        for k,v in so.items():
            if k!=last:
                soon[v]=k
                last=k
                i+=1
            else:
                soon[v]=k
            if i==3:
                break
        #sooner= {'NXF543900R':4,'NXF79434lj':3, 'NXF098321Y'}
        return soon##TODO: RETURN VALUE AS PER THE DESCRIPTION
    
    
    
    def find_closing_date(self,start_date,end_date):
        # Write your code
        ddd= {}
        ##l=[start_date,end_date]
        #ed= ut.convert_date(end_date)
        #sd= ut.convert_date(start_date)
        #diff= ed - sd
        #d= diff.days
        sql="SELECT * FROM Car WHERE no_of_days>3"
        cursor.execute(sql)
        db_data= cursor.fetchall()
        for i in db_data:
            q1= i[5] - start_date
            q2= end_date - i[5]
            if q1>=timedelta(days=0) and q2>=timedelta(days=0) and i[4]>3:
                closing_rental_date= i[5]+timedelta(days=i[4])
                ddd[i[0]]= closing_rental_date
        return ddd##TODO: RETURN VALUE AS PER THE DESCRIPTION
    
    
    
    
   
        
	

# # Please do not change the skelecton code given here
# # You can add any number of methods and attributes as you required without changing the given template

import ticket as tt
import utility
import cx_Oracle

db=""
with open('database.properties') as f:
    lines = [line.strip().split("=") for line in f.readlines() if not line.startswith('#') and line.strip()]
    db = {key.strip(): value.strip() for key, value in lines}
   
#Creating Connection String
conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
cursor=conn.cursor()

class TicketReservation:
    
    def __init__(self):
        self.__ticket_details_list=[]
        
    
    
    def build_ticket_details(self, ticket_details):
        # Write your code here
        for ticket in ticket_details:
            regs=ticket.split(",")
            check=utility.validate_ticket_id(regs[0])
            if check==True:
                dt=utility.convert_date(regs[2])
                t_obj=tt.Ticket(regs[0],regs[1],dt,regs[3],regs[4],regs[5],regs[6],float(regs[7]),int(regs[8]))
                t_obj.calculate_bill_amount()
                self.__ticket_details_list.append(t_obj)
            else:
                print(check)
        return self.__ticket_details_list  #TODO CHANGE THIS RETURN VALUE
    
    
    
    
    def add_ticket_details(self, ticket_list):
        # Write your code here
        cursor=conn.cursor()
        query="""INSERT INTO ticket(ticket_id, customer_name, purchase_date, travel_type, source, destination, ticket_type, no_of_km, no_of_tickets, bill_amount)
                VALUES(:0,:1,:2,:3,:4,:5,:6,:7,:8,:9)"""
        for i in ticket_list:
            li=[]
            li.append(i.get_ticket_id())
            li.append(i.get_customer_name())
            li.append(i.get_purchase_date())
            li.append(i.get_travel_type())
            li.append(i.get_source())
            li.append(i.get_destination())
            li.append(i.get_ticket_type())
            li.append(i.get_no_of_km())
            li.append(i.get_no_of_tickets())
            li.append(i.get_bill_amount())
            cursor.execute(query, li)
            conn.commit()
        cursor.close()
        
        
        return None  #TODO CHANGE THIS RETURN VALUE
    
    
    def search_ticket_id(self, ticket_id):
       # Write your code here
        cursor=conn.cursor()
        query="""SELECT * FROM ticket WHERE ticket_id=:ticket_id"""
        cursor.execute(query, [ticket_id])
        data=cursor.fetchone()
        cursor.close()
        if data is None:
            return None
        else:    
            s_obj=tt.Ticket(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
            s_obj.calculate_bill_amount()
            return s_obj #TODO CHANGE THIS RETURN VALUE
        
    
    def update_bill_amount(self, no_of_tickets):
        # Write your code here
        lis = []
        cursor=conn.cursor()
        query="""UPDATE ticket SET bill_amount=0.7*bill_amount WHERE no_of_tickets>:01"""
        cursor.execute(query, [no_of_tickets])
        query="""SELECT *
        FROM ticket
        WHERE no_of_tickets>:01"""
        cursor.execute(query,[no_of_tickets])
        fetchs = cursor.fetchall()
        cursor.close()
        if fetchs is None:
            return lis
        else:
            for fetch in fetchs:
                f_obj=tt.Ticket(fetch[0],fetch[1],fetch[2],fetch[3],fetch[4],fetch[5],fetch[6],float(fetch[7]),int(fetch[8]))
                f_obj.calculate_bill_amount()
                lis.append(f_obj)
            return lis
     #TODO CHANGE THIS RETURN VALUE
    
        
    
	            
               
        
        
        
            
            
        
	    
	

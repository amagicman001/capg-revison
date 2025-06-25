# Please do not change the skelecton code given here.
# Write your code only in the provided places alone

class Ticket:
    
    # Define the parameterized constructor here
    def __init__(self, ticket_id, customer_name, purchase_date, travel_type, source, destination, ticket_type, no_of_km, no_of_tickets):
        self.__ticket_id=ticket_id #no
        self.__customer_name=customer_name #no
        self.__purchase_date=purchase_date #no
        self.__travel_type=travel_type #no
        self.__source=source #no
        self.__destination=destination #no
        self.__ticket_type=ticket_type #no
        self.__no_of_km=no_of_km #no
        self.__no_of_tickets=no_of_tickets #no
        self.__bill_amount=0.0

    def get_ticket_id(self):
        return self.__ticket_id

    def get_customer_name(self):
        return self.__customer_name

    def get_purchase_date(self):
        return self.__purchase_date

    def get_travel_type(self):
        return self.__travel_type

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_ticket_type(self):
        return self.__ticket_type

    def get_no_of_km(self):
        return self.__no_of_km

    def get_no_of_tickets(self):
        return self.__no_of_tickets

    def get_bill_amount(self):
        return self.__bill_amount

    # Setter methods
    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_purchase_date(self, purchase_date):
        self.__purchase_date = purchase_date

    def set_travel_type(self, travel_type):
        self.__travel_type = travel_type

    def set_source(self, source):
        self.__source = source

    def set_destination(self, destination):
        self.__destination = destination

    def set_ticket_type(self, ticket_type):
        self.__ticket_type = ticket_type

    def set_no_of_km(self, no_of_km):
        self.__no_of_km = no_of_km

    def set_no_of_tickets(self, no_of_tickets):
        self.__no_of_tickets = no_of_tickets

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount
    
    def calculate_bill_amount(self):
        ## Fill your code here
        if self.__travel_type=="Bus":
            if self.__ticket_type=="Sleeper":
                price=5.0
            elif self.__ticket_type=="SemiSleeper":
                price=2.0
        elif self.__travel_type=="Train":
            if self.__ticket_type=="Ac":
                price=6.0
            elif self.__ticket_type=="NonAc":
                price=4.0
        elif self.__travel_type=="Aeroplane":
            if self.__ticket_type=="Economy":
                price=8.0
            elif self.__ticket_type=="Business":
                price=15.0
            elif self.__ticket_type=="First":
                price=22.0
        bill_amt = (float(self.__no_of_km)*price)*float(self.__no_of_tickets)
        self.__bill_amount=bill_amt

        
    
        
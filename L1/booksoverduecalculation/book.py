# Please do not change the skelecton code given here.
# Write your code only in the provided places alone


class Book:
    
    def __init__(self,book_id,title,author,publish_date,book_type,days_overdue):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__publish_date=publish_date
        self.__book_type=book_type
        self.__days_overdue=days_overdue
        
        self.__overdue_amount=0.0

        
    def set_book_id(self, book_id):
        self.__book_id = book_id
        
    def get_book_id(self):
        return self.__book_id
    
    def set_title(self, title):
        self.__title = title
        
    def get_title(self):
        return self.__title
    
    def set_author(self, author):
        self.__author = author
        
    def get_author(self):
        return self.__author
    
    def set_publish_date(self, publish_date):
        self.__publish_date = publish_date
        
    def get_publish_date(self):
        return self.__publish_date
    
    def set_book_type(self, book_type):
        self.__book_type = book_type

    def get_book_type(self):
        return self.__book_type
    
    def set_days_overdue(self, days_overdue):
        self.__days_overdue = days_overdue

    def get_days_overdue(self):
        return self.__days_overdue
    
    def set_overdue_amount(self, overdue_amount):
        self.__overdue_amount = overdue_amount

    def get_overdue_amount(self):
        return self.__overdue_amount
    
    
    
    
    def calculate_overdue_amount(self):
        # Write your code here
        if self.__book_type=="Fiction":
            overam=(self.__days_overdue)*10.0
            self.__overdue_amount=overam
        elif self.__book_type=="Non-Fiction":
            overam=(self.__days_overdue)*7.0
            self.__overdue_amount=overam
        elif self.__book_type=="Children":
            overam=(self.__days_overdue)*5.5
            self.__book_type=overam
        

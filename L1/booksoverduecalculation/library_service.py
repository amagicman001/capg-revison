# Please do not change the skeleton code given here
# You can add any number of methods and attributes as you required without changing the given template

import book as bk
import utility
import cx_Oracle

db=""
with open('database.properties') as f:
    lines = [line.strip().split("=") for line in f.readlines() if not line.startswith('#') and line.strip()]
    db = {key.strip(): value.strip() for key, value in lines}

class LibraryService:
    
    def __init__(self):
        self.__book_list=[]
        
    def set_book_list(self, book_list):
        self.__book_list = book_list
        
    def get_book_list(self):
        return self.__book_list
    
    def build_book_details(self, book_records):
        # Write your code here
        self.__book_list = []
        for record in book_records:
            # Split the colon-separated record
            parts = record.split(':')
            if len(parts) == 6:
                book_id, title, author, publish_date_str, book_type, days_overdue = parts
                
                # Validate book ID
                if utility.validate_book_id(book_id):
                    # Convert date
                    publish_date = utility.convert_date(publish_date_str)
                    if publish_date:
                        # Create Book object
                        book_obj = bk.Book(book_id, title, author, publish_date, book_type, int(days_overdue))
                        # Calculate overdue amount
                        book_obj.calculate_overdue_amount()
                        # Add to book list
                        self.__book_list.append(book_obj)
        
    def add_book_details(self):
        # Write your code here
        try:
            conn = cx_Oracle.connect(db['DB_USERNAME'], db['DB_PASSWORD'], db['DSN'])
            cursor = conn.cursor()
            
            # Insert each book into database
            for book in self.__book_list:
                sql = """INSERT INTO library (book_id, title, author, publish_date, book_type, days_overdue, overdue_amount) 
                         VALUES (:1, :2, :3, :4, :5, :6, :7)"""
                cursor.execute(sql, [
                    book.get_book_id(),
                    book.get_title(),
                    book.get_author(),
                    book.get_publish_date(),
                    book.get_book_type(),
                    book.get_days_overdue(),
                    book.get_overdue_amount()
                ])
            
            conn.commit()
            cursor.close()
            conn.close()
            
        except cx_Oracle.Error as err:
            print(f"Database error: {err}")
        
    def search_book_id(self, book_id):
        # Write your code here
        try:
            conn = cx_Oracle.connect(db['DB_USERNAME'], db['DB_PASSWORD'], db['DSN'])
            cursor = conn.cursor()
            
            sql = "SELECT * FROM library WHERE book_id = :1"
            cursor.execute(sql, [book_id])
            result = cursor.fetchone()
            
            cursor.close()
            conn.close()
            
            if result:
                # Create Book object from database result
                book_obj = bk.Book(result[0], result[1], result[2], result[3], result[4], result[5])
                book_obj.set_overdue_amount(result[6])
                return book_obj
            else:
                return None
                
        except cx_Oracle.Error as err:
            print(f"Database error: {err}")
            return None
        
    def delete_book_details(self, days_overdue):
        # Write your code here
        try:
            conn = cx_Oracle.connect(db['DB_USERNAME'], db['DB_PASSWORD'], db['DSN'])
            cursor = conn.cursor()
            
            # Delete records where days_overdue > given days_overdue
            sql = "DELETE FROM library WHERE days_overdue > :1"
            cursor.execute(sql, [days_overdue])
            conn.commit()
            
            # Get remaining records
            sql = "SELECT book_id, title, days_overdue FROM library"
            cursor.execute(sql)
            results = cursor.fetchall()
            
            cursor.close()
            conn.close()
            
            # Create dictionary with book_id as key and [title, days_overdue] as value
            result_dict = {}
            for row in results:
                book_id, title, days_overdue_val = row
                result_dict[book_id] = [title, days_overdue_val]
            
            return result_dict
            
        except cx_Oracle.Error as err:
            print(f"Database error: {err}")
            return None
# Please do not change the skeleton code given here.
# Fill the code only in the provided places alone
import utility
import library_service as lse

def main():
    # Write the appropriate code here as per the specifications
    service = lse.LibraryService()
    
    # Read file and build book details
    file_data = utility.read_file('input.txt')
    service.build_book_details(file_data)
    
    # Add book details to database
    service.add_book_details()
    
    # Get user input for book ID search
    book_id = input("Enter the Book ID to be searched: ")
    
    
    if utility.validate_book_id(book_id):
            book = service.search_book_id(book_id)
            if book:
                print(f"Book ID: {book.get_book_id()}")
                print(f"Title: {book.get_title()}")
                print(f"Author: {book.get_author()}")
                print(f"Publish Date: {book.get_publish_date()} 00:00:00")
                print(f"Book Type: {book.get_book_type()}")
                print(f"Days Overdue: {book.get_days_overdue()}")
                print(f"Overdue Amount: {book.get_overdue_amount()}")
            else:
                print("No details found")

    
    print()
    
    # Get user input for days overdue
    days_overdue = int(input("Enter the number of overdue days: "))
    
    # Delete book details and get remaining books
    remaining_books = service.delete_book_details(days_overdue)
    
    if remaining_books:
        print("Remaining Books after deletion:")
        for book_id, details in remaining_books.items():
            title, days_overdue_val = details
            print(f"Book ID: {book_id}, Title: {title}, Days Overdue: {days_overdue_val}")
    
if __name__ == "__main__":
    main()
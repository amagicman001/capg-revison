# Please do not change the skelecton code given here.
# Fill the code only in the provided places alone

import utility
import ticket_reservation as tr

def main():
    # # Write the appropriate code here as per the specifications
    lis=utility.read_file('input.txt')
    tr_obj=tr.TicketReservation()
    bt=tr_obj.build_ticket_details(lis)
    tr_obj.add_ticket_details(bt)
    tid=input("Enter the ticket number to be searched: ")
    check = utility.validate_ticket_id(tid)
    if check== True:
        t_obj=tr_obj.search_ticket_id(tid)
        if t_obj is None:
            print("No details found")
        
        # noft=input("\nEnter the Number of days to give discount: ")
        # lis=tr_obj.update_bill_amount(noft)
    #     if lis is None:
    #         print("No Records updated")
    #     else:
    #         print("The updated record details are:")
    #         print(f"Ticket id: {lis[0]}")
    #         print(f"Customer Name: {lis[1]}")
    #         print(f"Travel Type: {lis[2]}")
    #         print(f"Source: {lis[3]}")
    #         print(f"Destination: {lis[4]}")
    #         print(f"Ticket Type: {lis[5]}")
    #         print(f"No of km: {lis[6]}")
    #         print(f"No of Tickets: {lis[7]}")
    #         print(f"Total cost: {lis[8]}")

    pass
if __name__ == "__main__":
    main()

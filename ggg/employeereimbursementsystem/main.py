# Please do not change the skelecton code given here.
# Fill the code only in the provided places alone

import emp_reimbursement_service as rs
import utility as ut

def main():
    # Write the appropriate code here as per the specifications
    app= rs.EmpReimbursementService()
    l_obj= app.get_emp_reimbursement_details("input.txt")
    app.add_reimbursement_details(l_obj)
    request_id=input("Enter the request id:")
    valid= ut.validate_request_id(request_id)
    # Write the appropriate code here fordisplaying the reibursement request details as per the specifications
    if valid==True:
        obj= app.search_reimbursement_request(request_id)
        if obj is None:
            print("No record found")
        else:
            print("")
            print("Request Id:",obj.get_request_id())
            print("Employee Code:",obj.get_employee_code())
            print("Date of Travel:",obj.get_date_of_travel())            
            print("No.of Days:",obj.get_no_of_days_of_stay())
            print("Accommodation Cost:",obj.get_accomodation_cost())
            print("Dining Cost:",obj.get_dining_cost())
            print("Local Travel cost:",obj.get_local_travel_cost())
            print("Allowances:",obj.get_allowances())
            print("Total Reimbursement Amount:",obj.get_total_reimbursement_cost())
    else:
        print(valid)
    no_days=int(input("\n\nEnter the no. of days for giving expense increment:"))
    objs= app.update_costs(no_days)
    # Write the appropriate code here for displaying the increment details as per the specifications
    if objs is None:
        print("No Records updated")
    else:
        for obj in objs:
            print("")
            print("Request Id:",obj.get_request_id())
            print("Employee Code:",obj.get_employee_code())
            print("Date of Travel:",obj.get_date_of_travel())            
            print("No.of Days:",obj.get_no_of_days_of_stay())
            print("Accommodation Cost:",obj.get_accomodation_cost())
            print("Dining Cost:",obj.get_dining_cost())
            print("Local Travel cost:",obj.get_local_travel_cost())
            print("Allowances:",obj.get_allowances())
            print("Total Reimbursement Amount:",obj.get_total_reimbursement_cost())


if __name__ == "__main__":
    main()

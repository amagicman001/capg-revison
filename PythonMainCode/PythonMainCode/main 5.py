# Please do not change the skelecton code given here.
# Fill the code only in the provided places alone

import utility as ut
import car_service as cs

def main():
    # Write the appropriate code here as per the specifications
    f_data= ut.access_file("CarDetails.txt")
    app= cs.CarService()
    app.read_data(f_data)
    # Write the appropriate code here as per the specifications to call 'find_top3_rentals' method
    x= app.find_top3_rentals()
    print("Top 3 rentals:")
    for k,v in x.items():
        print(k,":",v)
    print("")
    start_date=input("Enter the start rental date to search:")
    end_date=input("Enter the end rental date to search:")
    sd= ut.convert_date(start_date)
    ed= ut.convert_date(end_date)
    ddd= app.find_closing_date(sd,ed)
    print("The closing rental date of cars with the specified rental date is/are:")
    if len(ddd)==0:
        print("No cars taken for rental in the specified date range")
    else:
        for k,v in ddd.items():
            print(k,":",v)
    # Write the appropriate code here as per the specifications
    



if __name__ == "__main__":
    main()

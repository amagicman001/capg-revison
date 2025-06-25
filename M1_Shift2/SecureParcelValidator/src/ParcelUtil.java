
import java.util.regex.Pattern;



public class ParcelUtil {

    public boolean validateParcelId(String parcelId) throws InvalidParcelException {
        if(Pattern.matches("^PC-[1-9]{5}", parcelId)) {
        	return true;
        }
        else {
        	throw new InvalidParcelException("The parcel Id "+parcelId+" is invalid");
        }
    }

    public boolean validateDestination(String destination) throws InvalidParcelException {
        if(destination=="New York"||destination=="Los Angeles"||destination=="Chicago"||destination=="Houston") {
        	return true;
        }else {
        	throw new InvalidParcelException("The destination "+destination+" is invalid");
        }
    }

    public boolean validateParcelWeight(double weight, String destination) throws InvalidParcelException {
        if(destination=="New York"&&(weight<=30 && weight>0)){
        	return true;
        }
        else if(destination=="LosAngeles"&&(weight<=50&&weight>0)){
        	return true;
        }
        else if(destination=="Chicago"&&(weight<=25&&weight>0)) {
        	return true;
        }
        else if(destination=="Houston"&&(weight<=40&&weight>0)) {
        	return true;
        }else {
        	throw new InvalidParcelException("The weight "+weight+" kg is invalid for "+destination);
        }
	
    }
    
    public double calculateShippingCost(String destination, double weight) throws InvalidParcelException {
       if(destination=="New York"&&weight!=0) {
    	   return 10*weight;
       }else if(destination=="Los Angeles"&&weight!=0) {
    	   return 8*weight;
       }else if(destination=="Chicago"&&weight!=0){
    	   return 12*weight;
       }
       else if(destination=="Houston"&&weight!=0) {
    	   return 9*weight;
       }else {
	      throw new InvalidParcelException("Invalid weight for "+destination);
        
    }
}
    
}
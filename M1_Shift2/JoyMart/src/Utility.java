import java.util.regex.Pattern;

public class Utility {

	public Product parseDetails(String productDetails) {
		Product obj = null;

		// Fill the code here

		return obj;

	}

	public boolean validateProductId(String productId) {
		if(Pattern.matches("^JOY[0-9]{3}[A-Z]&", productId)) {
			return true;
		}else {
			return false;
		}
	}
	
	public String findObjectType(Product product) {
	    return null;
	}

}

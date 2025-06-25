public class Garments extends Product {
	
	public Garments(String productId,String productBarcode,String garmentsName,int noOfGarments,int garmentsPrice) {
		super(productId, productBarcode);
		this.garmentsName=garmentsName;
		this.noOfGarments=noOfGarments;
		this.garmentsPrice=garmentsPrice;
	}

	private String garmentsName;
	private int noOfGarments;
	private int garmentsPrice;
	
    

	public int getGarmentsPrice() {
		return garmentsPrice;
	}

	public void setGarmentsPrice(int garmentsPrice) {
		this.garmentsPrice = garmentsPrice;
	}

	public String getGarmentsName() {
		return garmentsName;
	}

	public void setGarmentsName(String garmentsName) {
		this.garmentsName = garmentsName;
	}

	public int getNoOfGarments() {
		return noOfGarments;
	}

	public void setNoOfGarments(int noOfGarments) {
		this.noOfGarments = noOfGarments;
	}

	public double getVehicleCharge() {
       if(noOfGarments<1000) {
    	   return 1000.00;
       }else if(noOfGarments>=1000 && noOfGarments<=1800) {
    	   return 2000.00;
       }else {
    	   return 3000.00;
       }
	}

	public double calculateTotalBill() {
      return (garmentsPrice*noOfGarments)+getVehicleCharge()+(garmentsPrice*noOfGarments*0.3);
	}

}

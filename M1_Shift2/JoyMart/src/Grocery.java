public class Grocery extends Product {

	public Grocery(String productId, String productBarcode,String itemName,int weight,int itemPrice) {
		super(productId, productBarcode);
		this.itemName=itemName;
		this.weight=weight;
		this.itemPrice=itemPrice;
		
	}

	private String itemName;
	private int weight;
	private int itemPrice;

	public int getItemPrice() {
		return itemPrice;
	}

	public void setItemPrice(int itemPrice) {
		this.itemPrice = itemPrice;
	}

	public String getItemName() {
		return itemName;
	}

	public void setItemName(String itemName) {
		this.itemName = itemName;
	}

	public int getWeight() {
		return weight;
	}

	public void setWeight(int weight) {
		this.weight = weight;
	}

	

	public double calculateTotalBill() {
		return (itemPrice*weight)+(getVehicleCharge())+(itemPrice*weight*0.3);
	}

	public double getVehicleCharge() {

		if(weight<300) {
			return 1000.00;
		}else if(weight>=300 && weight<=600){
			return 2000.00;
		}else {
			return 3000.00;
		}
	}

}

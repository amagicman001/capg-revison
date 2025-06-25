abstract public class Product {
	protected String productId;
	protected String productBarcode;

	public String getProductId() {
		return productId;
	}

	public void setProductId(String productId) {
		this.productId = productId;
	}

	public String getProductBarcode() {
		return productBarcode;
	}

	public void setProductBarcode(String productBarcode) {
		this.productBarcode = productBarcode;
	}

	public Product(String productId,String productBarcode) {
		this.productId=productId;
		this.productBarcode=productBarcode;
	}

	abstract public double getVehicleCharge();
	abstract public double calculateTotalBill();

}

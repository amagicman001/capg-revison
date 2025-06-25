
public class Painting {
    private String paintingId;
    private String paintingName;
    private double estimatedWorth;
    private String artistName;
    
    public Painting(){}
    
    public Painting(String paintingId, String paintingName, double estimatedWorth, String artistName) {
        this.paintingId = paintingId;
        this.paintingName = paintingName;
        this.estimatedWorth = estimatedWorth;
        this.artistName = artistName;
    }

    
    public String getPaintingId() {
        return paintingId;
    }

    public String getPaintingName() {
        return paintingName;
    }

    public String getArtistName() {
        return artistName;
    }

    public double getEstimatedWorth() {
        return estimatedWorth;
    }
    
    public void setPaintingId(String paintingId) {
		this.paintingId = paintingId;
	}

	public void setPaintingName(String paintingName) {
		this.paintingName = paintingName;
	}

	public void setArtistName(String artistName) {
		this.artistName = artistName;
	}

	public void setEstimatedWorth(double estimatedWorth) {
		this.estimatedWorth = estimatedWorth;
	}
	
	

	
}
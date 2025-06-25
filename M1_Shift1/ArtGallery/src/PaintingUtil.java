import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class PaintingUtil {
    private List<Painting> paintingList = new ArrayList<>();

    public List<Painting> getPaintingList() {
		return paintingList;
	}

	public void setPaintingList(List<Painting> paintingList) {
		this.paintingList = paintingList;
	}

	public void addPaintingDetails(Painting painting) {
        paintingList.add(painting);
    }
    
	public Painting getPaintingById(String paintingId) {
		for(Painting p:paintingList) {
			if(p.getPaintingId().equals(paintingId)) {
				return p;
			}
		}
		return null;
	}
  
    public List<Painting> getMostValuablePaintings() {
    	List<Painting> resultList=new ArrayList<Painting>();
    	double high=0;
        for(Painting obj:paintingList) {
    	   high=obj.getEstimatedWorth();
    	   if(obj.getEstimatedWorth()>high) {
    		   high=obj.getEstimatedWorth();
    	   }
       }
        return resultList;
    }
}


import java.util.Scanner;

public class UserInterface {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PaintingUtil obj=new PaintingUtil();
        
        System.out.println("Enter the number of paintings to be added");
        int number =scanner.nextInt();
        System.out.println("Enter painting details");
        for(int i=0;i<number;i++) {
        	String[] input=scanner.nextLine().split(":");
        	String paintingIid=input[0];
        	String paintingname=input[1];
        	double estimatedworth=Double.parseDouble(input[2]);
        	String artistname=input[3];
        	obj.addPaintingDetails(new Painting(paintingIid,paintingname, estimatedworth,artistname));
        }
        
        System.out.println("Enter the Painting Id to check worth");
        String id=scanner.nextLine();
        
        
    }
}
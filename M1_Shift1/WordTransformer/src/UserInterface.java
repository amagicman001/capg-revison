import java.util.Arrays;
import java.util.Scanner;

public class UserInterface {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
       System.out.println("Enter the first word");
        String first=scanner.nextLine();
        String [] valid=first.split(" ");
        if(valid.length>1) {
        	System.out.println(first+" is an invalid word");
        	return;
        }
        System.out.println("Enter the second word");
        String second=scanner.nextLine();
        String[] valid2=second.split(" ");
        if(valid2.length>1) {
        	System.out.println(second+" is an invalid word");
        }
        
        
        char[] f = first.toLowerCase().toCharArray();
        char[]fs=first.toLowerCase().toCharArray();
        char[] s= second.toLowerCase().toCharArray();
        
        Arrays.sort(f);
        Arrays.sort(s);
        StringBuilder sb=new StringBuilder();
        if(Arrays.equals(f, s)) {
        	for(int i=0;i<fs.length;i++) {
        		if(i%2!=0) {
        			sb.append("*");
        		}else {
        			sb.append(fs[i]);
        		}
        		
        	}
        	System.out.println(sb.toString());
        }else {
        	StringBuilder SB=new StringBuilder(first);
        	SB.append("#").append(second).reverse();
            
        	String str=SB.toString();
        	char [] result =str.toCharArray();
        	StringBuilder ans = new StringBuilder();
        	for(int i=0;i<result.length;i++) {
        		if(result[i]=='a'||result[i]=='e'||result[i]=='i'||result[i]=='o'||result[i]=='u'||result[i]=='A'||result[i]=='E'||result[i]=='O'||result[i]=='U') {
        			ans.append('#');
        		}else {
        			ans.append(result[i]);
        		}
        	}
        	System.out.println(ans.toString());
        	
        	
        	
        }
        
    }
}

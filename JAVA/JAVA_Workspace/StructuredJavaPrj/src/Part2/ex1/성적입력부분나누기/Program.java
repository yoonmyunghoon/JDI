package Part2.ex1.성적입력부분나누기;

import java.util.Scanner;

public class Program{
	
    public static void main(String[] args) {
    	
    	int[] kors = new int[3];
    	
        int total = 0;
        float avg;
        int menu;
        boolean keepLoop = true;			
		
		Scanner scan = new Scanner(System.in);
		
		while(keepLoop)
		{
			System.out.println("|---------------------|");
			System.out.println("|       Main menu     |");
			System.out.println("|---------------------|");
			System.out.println("\t1.성적 입력");
			System.out.println("\t2.성적 출력");
			System.out.println("\t3.종료");
			System.out.print("\t>");
	        menu = scan.nextInt();
	        
	        switch(menu) {	        
	        case 1:
	        	
	        	System.out.println("|---------------------|");
				System.out.println("|       Score in      |");
				System.out.println("|---------------------|");
		        System.out.println();
		       		        
		        for(int i=0; i<3; i++)
			        do {
			        	System.out.printf("국어%d : ", i+1);
				        kors[i] = scan.nextInt();
			        
				        if(kors[i] < 0 || 100 < kors[i])
				        	System.out.println("out of scope 0~100");
				        
			        }while(kors[i] < 0 || 100 < kors[i]);
		        
		        System.out.println("|---------------------|");
	        	       
		        break;
	        case 2:
		        
		        for(int i=0; i<3; i++)
		        	total += kors[i];
		        
		        avg = total / 3.0f;
		        
		        System.out.println("|---------------------|");
				System.out.println("|      Score out      |");
				System.out.println("|---------------------|");
		        System.out.println();		        
		       
		        for(int i=0;i<3;i++)
		        	System.out.printf("국어%d : %3d\n", i+1, kors[i]);    	
		        	        
		        System.out.printf("총점 : %3d\n", total);
				System.out.printf("평균 : %6.2f\n", avg);
				System.out.println("|---------------------|");
	        	
		        break;
	        case 3:
	        	System.out.println("Bye~~");
	        	
	        	keepLoop = false;
				break;
	        
	        default:
	        	System.out.println("1~3까지만 입력해주세요.");
	       
	        }
		}
    }
}

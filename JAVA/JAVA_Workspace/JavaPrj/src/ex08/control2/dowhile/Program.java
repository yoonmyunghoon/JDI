package ex08.control2.dowhile;

import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		
		
		Scanner scan = new Scanner(System.in);
		
		int a = 0;
		int b = 0;
		int c = 0;
		
		
		while(true) {
			//------------성적 입력 부분------------------------------
			System.out.println("|---------------------|");
			System.out.println("|       Score in      |");
			System.out.println("|---------------------|");
			
			do {
				System.out.print("국어1 : ");
				a = scan.nextInt();
				if(a < 0 || 100 < a) {
					System.out.println("out of scope 0~100");
				}
				
			} while(a < 0 || 100 < a);
			
			do {
				System.out.print("국어2 : ");
				b = scan.nextInt();
				if(b < 0 || 100 < b) {
					System.out.println("out of scope 0~100");
				}
				
			} while(b < 0 || 100 < b);
			
			do {
				System.out.print("국어3 : ");
				c = scan.nextInt();
				if(c < 0 || 100 < c) {
					System.out.println("out of scope 0~100");
				}
				
			} while(c < 0 || 100 < c);
			
			
			
	
			//------------성적 출력 부분------------------------------
			int total = a + b + c;
			float avg = total / 3.0f;
			
			System.out.println("|---------------------|");
			System.out.println("|      Score out      |");
			System.out.println("|---------------------|");
			
			System.out.print("국어1 : ");
			System.out.print(a);
			System.out.println();
			System.out.printf("국어2 : %3d\n", b);
			System.out.printf("국어3 : %3d\n", c);
			System.out.printf("총점 : %3d\n", total);
			System.out.printf("평균 : %6.2f\n", avg);
			System.out.println("|---------------------|");
		}
	}
}
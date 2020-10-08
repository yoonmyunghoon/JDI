package ex6.operator;

import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		
		
		Scanner scan = new Scanner(System.in);
		
		int a = 0;
		int b = 0;
		int c = 0;
		
		
		//------------성적 입력 부분------------------------------
		System.out.println("|---------------------|");
		System.out.println("|       Score in      |");
		System.out.println("|---------------------|");
		System.out.print("국어1 : ");
		a = scan.nextInt();
		System.out.print("국어2 : ");
		b = scan.nextInt();
		System.out.print("국어3 : ");
		c = scan.nextInt();
		
		
		System.out.println(0 <= a && a <= 100 ? "ok" : "no");
		

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
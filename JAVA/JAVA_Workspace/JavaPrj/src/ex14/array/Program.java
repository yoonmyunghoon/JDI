package ex14.array;

import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		
//		int kor1, kor2, kor3;
		int [] kors = new int[3];
		int total;
		float avg;
		int menu;
		
		Scanner scan = new Scanner(System.in);
		
		
//		kor1 = 0;
//		kor2 = 0;
//		kor3 = 0;
		
		for(int i=0; i<3; i++) {
			kors[i] = 0;
		}
		
		종료:
		while(true) {
			//------------메인 메뉴 부분------------------------------
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
				//------------성적 입력 부분------------------------------
				System.out.println("|---------------------|");
				System.out.println("|       Score in      |");
				System.out.println("|---------------------|");
				
//				do {
//					System.out.print("국어1 : ");
//					kor1 = scan.nextInt();
//					if(kor1 < 0 || 100 < kor1) {
//						System.out.println("out of scope 0~100");
//					}
//					
//				} while(kor1 < 0 || 100 < kor1);
//				
//				do {
//					System.out.print("국어2 : ");
//					kor2 = scan.nextInt();
//					if(kor2 < 0 || 100 < kor2) {
//						System.out.println("out of scope 0~100");
//					}
//					
//				} while(kor2 < 0 || 100 < kor2);
//				
//				do {
//					System.out.print("국어3 : ");
//					kor3 = scan.nextInt();
//					if(kor3 < 0 || 100 < kor3) {
//						System.out.println("out of scope 0~100");
//					}
//					
//				} while(kor3 < 0 || 100 < kor3);
				
				for(int i=0; i<3; i++) {
					do {
						System.out.printf("국어%d : ", i+1);
						kors[i] = scan.nextInt();
						if(kors[i] < 0 || 100 < kors[i]) {
							System.out.println("out of scope 0~100");
						}
						
					} while(kors[i] < 0 || 100 < kors[i]);
				}
			
				break;
				
			case 2: 
				//------------성적 출력 부분------------------------------
//				total = kor1 + kor2 + kor3;
				total = kors[0] + kors[1] + kors[2];
				avg = total / 3.0f;
				
				System.out.println("|---------------------|");
				System.out.println("|      Score out      |");
				System.out.println("|---------------------|");
				
				for(int i=0; i<3; i++) {
					System.out.printf("국어%d : %3d\n", i+1, kors[i]);
				}
						
				System.out.printf("총점 : %3d\n", total);
				System.out.printf("평균 : %6.2f\n", avg);
				System.out.println("|---------------------|");
			
				break;
				
			case 3: 
				break 종료;
				
			default:
				System.out.println("1~3까지만 입력해주세요.");
				
			}
		}
		System.out.println("good bye~");
	}
}
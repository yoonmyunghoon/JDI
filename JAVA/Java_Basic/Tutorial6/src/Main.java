// 조건문 & 반복문 

public class Main {

//	final static int N = 15;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		int score = 95;
//		
//		if(score >= 90) {
//			System.out.println("A");
//		} else if(score >= 80) {
//			System.out.println("B");
//		} else if(score >= 97) {
//			System.out.println("C");
//		} else {
//			System.out.println("F");
//		}
		
//		String a = "Man";
//		int b = 0;
		
		// 자바는 String을 비교할 때 equal()을 이용합니다.
		// 그 이유는 String은 다른 자료형과 다른 문자열 자료형이기 때문입니다.
		
//		if(a.equals("Man")) {
//			System.out.println("O");
//		} else {
//			System.out.println("X");
//		}
//		
//		if(b == 3) {
//			System.out.println("O");
//		} else {
//			System.out.println("X");
//		}
//		
//		if(a.equalsIgnoreCase("man") && b == 0) {
//			System.out.println("O");
//		} else {
//			System.out.println("X");
//		}
		
//		int i = 1, sum = 0;
//		while(i <= 1000) {
//			sum += i++;
//		}
//		System.out.println(sum);
		
//		for(int i = N; i > 0; i--) {
//			for(int j = i; j > 0; j--) {
//				System.out.print("*");
//			}
//			System.out.println();
//		}
		
		//x^2 + y^2 = r^2
//		for(int i = -N; i <= N; i++) {
//			for(int j = -N; j <= N; j++) {
//				if(i*i+j*j <= N*N) {
//					System.out.print("*");
//				} else {
//					System.out.print(" ");
//				}
//			}
//			System.out.println();
//		}
		
		int count = 0;
		
		for(;;) {
			System.out.println(count);
			count++;
			if (count==10) {
				break;
			}
		}
	}

}

//import java.util.Scanner;

// 배열 

public class Main {
	
	public static int max(int a, int b) {
		return (a>b) ? a : b;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		
//		Scanner scanner = new Scanner(System.in);
//		System.out.print("size: ");
//		int number = scanner.nextInt();
//		
//		int[] array = new int[number];
//		for(int i = 0; i < number; i++) {
//			System.out.print("number(>0): ");
//			array[i] = scanner.nextInt();
//		}
//		int result = -1;
//		for(int i = 0; i < number; i++) {
//			result = max(result, array[i]);
//		}
//		System.out.print("max: " + result);
		
		int[] array = new int[100];
		for(int i = 0; i < 100; i++) {
			array[i] = (int) (Math.random() * 100 + 1);
		}
		int sum = 0;
		for(int i = 0; i < 100; i++) {
			sum += array[i];
		}
		System.out.println(sum/100);
	}

}

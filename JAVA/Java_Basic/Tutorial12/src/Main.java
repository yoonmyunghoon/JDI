// 반복 함수와 재귀 함수 

public class Main {
	
	public static int fibonacci(int number) {
		int one = 1;
		int two = 1;
		int result = -1;
		if(number == 1) {
			return one;
		} else if(number == 2) {
			return two;
		} else {
			for(int i = 2; i < number; i++) {
				result = one + two;
				one = two;
				two = result;
			}
		}
		return result;
	}
	
	public static int fibonacciSelf(int number) {
		if(number == 1) {
			return 1;
		} else if(number == 2) {
			return 1;
		} else {
			return fibonacciSelf(number - 1) + fibonacciSelf(number - 2);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println(fibonacci(10));
		System.out.println(fibonacciSelf(10));

	}

}

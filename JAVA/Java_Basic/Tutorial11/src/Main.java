// 반복 함수와 재귀 함수 

public class Main {

	public static int factorial(int number) {
		int sum = 1;
		for(int i = 2; i <= number; i++) {
			sum *= i;
		}
		return sum;
	}
	
	public static int factorialSelf(int number) {
		if(number == 1) {
			return 1;
		} else {
			return number * factorialSelf(number - 1);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println(factorial(10));
		System.out.println(factorialSelf(10));
		
	}

}

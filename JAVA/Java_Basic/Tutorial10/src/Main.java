// 사용자 정의 함수

public class Main {
	
	public static int function(int number, int k) {
		for(int i = 1; i <= number; i++) {
			if(number%i==0) {
				k--;
				if(k==0) {
					return i;
				}
			}
		}
		return -1;
	}
	
	public static char function(String input) {
		return input.charAt(input.length() - 1);
	}
	
	public static int max(int a, int b) {
		return (a>b) ? a : b;
	}
	
	public static int maxThree(int a, int b, int c) {
		int result = max(a, b);
		result = max(result, c);
		return result;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int result = function(3050, 10);
//		if (result==-1) {
//			System.out.println("no");
//		} else {
//			System.out.println(result);
//		}
		
//		System.out.println(function("Hello world"));
		
		System.out.println(maxThree(345, 567, 789));
	}

}

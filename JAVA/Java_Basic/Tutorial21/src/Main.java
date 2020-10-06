import java.util.Scanner;

// 다형성(Polymorphism)

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("banana: 1, peach: 2");
		int input = scanner.nextInt();
		Fruit fruit;
		if(input == 1) {
			fruit = new Banana();
			fruit.show();
		} else if (input == 2) {
			fruit = new Peach();
			fruit.show();
		}
	}

}

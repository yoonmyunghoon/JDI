import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

// 기본 입출력 

public class Main {
 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		Scanner sc = new Scanner(System.in);
//		System.out.print("정수를 입력하세요");
//		int i = sc.nextInt();
//		System.out.print(i);
//		sc.close();
		
		
		File file = new File("input.txt");
		try {
			Scanner sc = new Scanner(file);
			while(sc.hasNextInt()) {
				System.out.println(sc.nextInt()*100);
			}
			sc.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			System.out.println("no file");
		}
	}

}

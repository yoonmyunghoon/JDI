import java.util.Scanner;

// 상속

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		Student student1 = new Student("Reynold", 26, 175, 67, "201827537", 1, 4.5);
//		Student student2 = new Student("Joice", 28, 165, 48, "201627537", 4, 4.3);
//		student1.show();
//		student2.show();
//		
//		Student[] students = new Student[100];
//		for(int i = 0; i < 100; i++) {
//			students[i] = new Student("aaa", 20, 175, 70, i+"", 1, 4.5);
//			students[i].show();
//		}
//				
//		Teacher teacher1 = new Teacher("nold", 46, 175, 67, "ADF1827", 3000000, 5);
//		Teacher teacher2 = new Teacher("nolden", 40, 155, 47, "ABF1827", 2800000, 4);
//		teacher1.show();
//		teacher2.show();
		
		Scanner sc = new Scanner(System.in);
		System.out.print("How many student?: ");
		int number = sc.nextInt();
		Student[] students = new Student[number];
		for(int i = 0; i < number; i++) {
			String name;
			int age;
			int height; 
			int weight; 
			String studentID;
			int grade;
			double gPA;
			System.out.print("name: ");
			name = sc.next();
			System.out.print("age: ");
			age = sc.nextInt();
			System.out.print("height: ");
			height = sc.nextInt();
			System.out.print("weight: ");
			weight = sc.nextInt();
			System.out.print("studentID: ");
			studentID = sc.next();
			System.out.print("grade: ");
			grade = sc.nextInt();
			System.out.print("gPA: ");
			gPA = sc.nextInt();
			students[i] = new Student(name, age, height, weight, studentID, grade, gPA);
		}
		
		for(int i = 0; i < number; i++) {
			students[i].show();
		}
		
	}

}

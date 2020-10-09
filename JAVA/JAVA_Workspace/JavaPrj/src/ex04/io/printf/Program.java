package ex04.io.printf;
public class Program {

	public static void main(String[] args) {
		
		int a = 60;
		int b = 40;
		int c = 30;
		int total = a + b + c;
		float avg = total / 3.0f;

		//------------성적 출력 부분------------------------------
		System.out.println("|---------------------|");
		System.out.println("|        Score        |");
		System.out.println("|---------------------|");
		
		System.out.print("국어1 : ");
		System.out.print(a);
		System.out.println();
		System.out.printf("국어2 : %3d\n", b);
		System.out.printf("국어3 : %3d\n", c);
		System.out.printf("총점 : %3d\n", total);
		System.out.printf("평균 : %6.2f\n", avg);
		System.out.println("|---------------------|");
		
		System.out.printf("%1$d %3$d %2$d\n", a, b, c);
		System.out.printf("%1$d %1$d %1$d", a);
		
//		System.out.print(80);
//		System.out.write(80);
//		System.out.flush();
//		System.out.printf("%d-%s-%s", 1995, "04", "08");
	}
}
package Part2.ex3.데이터구조화;

import java.util.Scanner;

public class ExamProgram{
	
    public static void main(String[] args) {
    	
    	Exam exam = new Exam();
    	
    	input(exam);
    	print(exam);

    }

	private static void print(Exam exam) {
		System.out.println("|---------------------|");
		System.out.println("|      Score out      |");
		System.out.println("|---------------------|");
        System.out.println();
        
        int kor = exam.kor;
        int eng = exam.eng;
        int math = exam.math;
        
        int total = kor+eng+math;
        float avg = total/3.0f;
        
        System.out.printf("국어 : %3d\n", kor);
        System.out.printf("영어 : %3d\n", eng);
        System.out.printf("수학 : %3d\n", math);
        
        System.out.printf("총점 : %3d\n", total);
		System.out.printf("평균 : %6.2f\n", avg);
		System.out.println("|---------------------|");
	}

	private static void input(Exam exam) {
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("|---------------------|");
		System.out.println("|       Score in      |");
		System.out.println("|---------------------|");
        System.out.println();
        
        int kor, eng, math;
        
        do {
        	System.out.printf("국어 : ");
	        kor = scan.nextInt();
        
	        if(kor < 0 || 100 < kor)
	        	System.out.println("out of scope 0~100");
	        
        }while(kor < 0 || 100 < kor);
        
        do {
        	System.out.printf("영어 : ");
        	eng = scan.nextInt();
        
	        if(eng < 0 || 100 < eng)
	        	System.out.println("out of scope 0~100");
	        
        }while(eng < 0 || 100 < eng);
        
        do {
        	System.out.printf("수학 : ");
        	math = scan.nextInt();
        
	        if(math < 0 || 100 < math)
	        	System.out.println("out of scope 0~100");
	        
        }while(math < 0 || 100 < math);
        
        exam.kor = kor;
        exam.eng = eng;
        exam.math = math;
		
	}
}


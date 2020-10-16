package Part3.ex5.추상화;

import java.util.Scanner;

public class ExamConsole {
	
//	private ExamList list = new ExamList();
	
	// 원래는 이렇게 생성자를 통해서 객체화하는 게 정상인데,
	// 컴파일러에서 위와 같이 적어도 이렇게 자동적으로 바꿔서 이해함 
	// 여기서는 이해를 위해 이렇게 변경하겠음
	// ExamConsole이 객체화되면 자동적으로 ExamList도 객체화
	// Composition Has A 상속관계
	private ExamList list;
	
	public ExamConsole() {
		list = new ExamList();
	}
	
	public void inputList() {
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
        
        
//        Exam exam = new Exam();
//        exam.setKor(kor); //exam.kor = kor;
//        exam.setEng(eng); //exam.eng = eng;
//        exam.setMath(math); //exam.math = math;
        
        
        Exam exam = new Exam(kor, eng, math);
        
        
//      -------------------------add----------------------------
        list.add(exam);
        
	}
	
	public void printList() {
		printList(list.size());
	}
	
	public void printList(int size) {
		System.out.println("|---------------------|");
		System.out.println("|      Score out      |");
		System.out.println("|---------------------|");
        System.out.println();
        
//        int size = list.current;
        if(size > list.size()) {
        	size = list.size();
        }
        
        for(int i=0; i<size; i++) {
	        Exam exam = list.get(i); // this.exams[i];
	        int kor = exam.getKor(); // exam.kor;
	        int eng = exam.getEng(); //exam.eng;
	        int math = exam.getMath(); //exam.math;
	        
	        int total = exam.total(); // kor+eng+math;
	        float avg = exam.avg(); // total/3.0f;
	        
	        System.out.printf("국어 : %d\n", kor);
	        System.out.printf("영어 : %d\n", eng);
	        System.out.printf("수학 : %d\n", math);
	        
	        System.out.printf("총점 : %3d\n", total);
			System.out.printf("평균 : %6.2f\n", avg);
			System.out.println("|---------------------|");
        }
		
	}

}

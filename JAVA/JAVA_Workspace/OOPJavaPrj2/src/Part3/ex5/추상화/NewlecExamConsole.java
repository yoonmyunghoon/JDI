package Part3.ex5.추상화;

import java.util.Scanner;

public class NewlecExamConsole extends ExamConsole{

	@Override
	protected Exam makeExam() {
		
		return new NewlecExam();
	}

	@Override
	protected void onInput(Exam exam) {
		NewlecExam newlecExam = (NewlecExam)exam;
		
		Scanner scan = new Scanner(System.in);
		int com;
		
		do {
        	System.out.printf("컴퓨터 : ");
        	com = scan.nextInt();
        
	        if(com < 0 || 100 < com)
	        	System.out.println("out of scope 0~100");
	        
        }while(com < 0 || 100 < com);
		
		newlecExam.setCom(com);
		
	}

	@Override
	protected void onPrint(Exam exam) {
		NewlecExam newlecExam = (NewlecExam)exam;
		int com = newlecExam.getCom();
		System.out.printf("컴퓨터 : %d\n", com);
		
	}

}

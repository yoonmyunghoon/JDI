package Part3.ex3.Getters와Setters;

import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		
		ExamList list = new ExamList();
		
		int menu;
        boolean keepLoop = true;
        
		while(keepLoop)
		{
			menu = inputMenu();
	        
	        switch(menu) {
	        case 1:
//	        	ExamList.inputList(list);
	        	list.inputList();
		        break;
	        case 2:
//	        	ExamList.printList(list);
	        	list.printList();
		        break;
	        case 3:
	        	System.out.println("Bye~~");
	        	keepLoop = false;
				break;
	        default:
	        	System.out.println("1~3까지만 입력해주세요.");
	        }
		}

	}

	static int inputMenu() {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	System.out.println("|---------------------|");
		System.out.println("|       Main menu     |");
		System.out.println("|---------------------|");
		System.out.println("\t1.성적 입력");
		System.out.println("\t2.성적 출력");
		System.out.println("\t3.종료");
		System.out.print("\t>");
        int menu = scan.nextInt();
        
        return menu;
    }

}

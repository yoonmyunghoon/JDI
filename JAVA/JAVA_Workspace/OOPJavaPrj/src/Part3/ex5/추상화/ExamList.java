package Part3.ex5.추상화;

public class ExamList {
	private Exam[] exams;
	private int current;
	
	public Exam get(int i) {
		
		return this.exams[i];
	}

	public void add(Exam exam) {
		Exam[] exams = this.exams;
        int size = this.current;
        
        if(exams.length == size) {
        	// 1. 크기가 5개 정도 더 큰 새로운 배열을 생성하시오.
        	Exam[] temp = new Exam[size+5];
        	// 2. 값을 이주시키기
        	for(int i=0; i<size; i++) {
        		temp[i] = exams[i];
        	}
        	// 3. list.exams가 새로 만든 temp배열을 참조하도록 한다.
        	this.exams = temp;
        }
        this.exams[this.current] = exam;
        this.current++;
		
	}
	
	// Aggregation Has A 상속 관계 
	public ExamList() {
//		this.exams = new Exam[3];
//		this.current = 0;
		
//		this생략가능, 식별해야할 경우엔 지우면 안됨
		exams = new Exam[3];
		current = 0;
	}

	
	public int size() {
		
		return current;
	}
}

import Part3.ex4.UI코드분리하기.Exam;

public class Program {

	public static void main(String[] args) {
		NewlecExam exam = new NewlecExam();
		exam.setKor(10);
		exam.setEng(10);
		exam.setMath(10);
		exam.setCom(10);
		
		System.out.println(exam.total());
		System.out.println(exam.avg());

	}

}

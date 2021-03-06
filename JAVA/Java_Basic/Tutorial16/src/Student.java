
public class Student extends Person {
	private String studentID;
	private int grade;
	private double GPA;
	public String getStudentID() {
		return studentID;
	}
	public void setStudentID(String studentID) {
		this.studentID = studentID;
	}
	public int getGrade() {
		return grade;
	}
	public void setGrade(int grade) {
		this.grade = grade;
	}
	public double getGPA() {
		return GPA;
	}
	public void setGPA(double gPA) {
		GPA = gPA;
	}
	public Student(String name, int age, int height, int weight, String studentID, int grade, double gPA) {
		super(name, age, height, weight);
		this.studentID = studentID;
		this.grade = grade;
		GPA = gPA;
	}
	
	public void show() {
		System.out.println("----------------------");
		System.out.println("name: " + getName());
		System.out.println("age: " + getAge());
		System.out.println("height: " + getHeight());
		System.out.println("weight: " + getWeight());
		System.out.println("studentID: " + getStudentID());
		System.out.println("grade: " + getGrade());
		System.out.println("GPA: " + getGPA());
	}
	
	
}

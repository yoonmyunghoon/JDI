// 객체(object)

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Archer archer1 = new Archer("ach1", "good");
		Archer archer2 = new Archer("ach1", "good");
		System.out.println(archer1 == archer2);
		System.out.println(archer1.equals(archer2));
		 
	}

}

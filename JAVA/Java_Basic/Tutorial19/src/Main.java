// 최종(Final)

public class Main extends Parent{
	
	public void show_() {
		System.out.println("Hello~~");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		final int number = 10;
		System.out.println(number);
		
		Main main = new Main();
		main.show();
		main.show_();
	}

}

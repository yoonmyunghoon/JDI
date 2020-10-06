// 추상(Abstract)

public class Main extends Player {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Main main = new Main();
		main.play("let it go");
		main.pause();
		main.stop();
		
		Dog dog = new Dog();
		Cat cat = new Cat();
		dog.crying();
		cat.crying();
	}

	@Override
	void play(String songName) {
		// TODO Auto-generated method stub
		
		System.out.println(songName+" play");
	}

	@Override
	void pause() {
		// TODO Auto-generated method stub
		System.out.println(" pause");
	}

	@Override
	void stop() {
		// TODO Auto-generated method stub
		System.out.println(" stop");
	}

}

# 구조적 프로그래밍



## 1. 프로그래밍과 프로그래밍 언어

### 동일한 프로그램이지만 방법을 달리 만들 수 있다.

- 자바 프로그래밍(절차지향) < 구조적인 프로그래밍 < 객체지향 프로그래밍
- 객체 지향으로 가기 전에 구조적 프로그래밍을 먼저 알아보자

### 구조적 프로그래밍이란?

- 프로그램의 크기가 커지면 단위별로 쪼개서 만든다
- 프로그래밍은 절차이다, 그 절차에 구조가 생긴다
- 절차를 자르는 도구로써의 함수
  - 함수가 가지는 능력: 코드를 잘라낼 수 있다
- 함수를 이용하면
  - 코드의 직접 사용을 차단할 수 있다
  - 코드를 작게 나누어서 만들 수 있다
  - 코드를 집중화할 수 있다
  - 코드를 재사용할 수 있다
- 자바로 함수를 정의하고 사용하는 방법

```java
// 함수 정의
static int power(int x) {
	return (x+3)*(x+3);
}

// 함수 사용
(power(7) + 3)*power(7);


// 반환 값이 없을 때 정의 방법
static void power(int x) {
	System.out.println((x+3)*(x+3));
}
```



## 2. 코드 구조화 Bottom Up 방식 연습1

- 절자적 프로그램을 쪼개서 구조적 프로그램을 만드는 방식: Bottom Up
- 처음부터 구조적 프로그램으로 설계하고 개발하는 방식: Top Down
- 여기서는 절차적인 프로그램을 짤라서 구조적 프로그램을 만들어보자

### 성정입력을 위한 코드를 새로운 함수에 담기

![create_function](Structured_JAVA_img/create_function.png)

- 외부 함수에 접근 불가능
- 변수를 바깥으로 빼줘야됨

![create_function1](Structured_JAVA_img/create_function1.png)

- 이렇게 하면 가능
- 전역 변수로 만들어서 접근할 수 있도록 만듬
- 좀 더 바람직한 방법이 있는데 그건 나중에..
- 전역변수가 되기 위해서는 static을 써야됨
  - 힘수 앞에 있는 static은 다른 의미
  - 함수 앞의 static은 이게 함수다 라고 하는 의미
  - 일반적인 메소드는 static을 뺌
- scanner는 전역으로 안함
  - 꼭 공유해야되는게 아니면 안하는게 좋음
  - 따로 써주자



## 3. 코드 구조화 Bottom Up 방식 연습2

```java
package Part2.ex1.성적입력부분나누기;

import java.util.Scanner;

public class StructuredProgram{
	
	static int[] kors = new int[3];
	
    public static void main(String[] args) {
    	
        int menu;
        boolean keepLoop = true;			
        
		while(keepLoop)
		{
			menu = 메뉴입력();
	        
	        switch(menu) {	        
	        case 1:
	        	성적입력();
		        break;
	        case 2:
		        성적출력();
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
    
    static int 메뉴입력() {
    	
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
    
    static void 성적출력() {
    	
    	int total = 0;
        float avg;
        
    	for(int i=0; i<3; i++)
        	total += kors[i];
        
        avg = total / 3.0f;
        
        System.out.println("|---------------------|");
		System.out.println("|      Score out      |");
		System.out.println("|---------------------|");
        System.out.println();		        
       
        for(int i=0;i<3;i++)
        	System.out.printf("국어%d : %3d\n", i+1, kors[i]);    	
        	        
        System.out.printf("총점 : %3d\n", total);
		System.out.printf("평균 : %6.2f\n", avg);
		System.out.println("|---------------------|");
    }
    
    static void 성적입력() {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	System.out.println("|---------------------|");
		System.out.println("|       Score in      |");
		System.out.println("|---------------------|");
        System.out.println();
       		        
        for(int i=0; i<3; i++)
	        do {
	        	System.out.printf("국어%d : ", i+1);
		        kors[i] = scan.nextInt();
	        
		        if(kors[i] < 0 || 100 < kors[i])
		        	System.out.println("out of scope 0~100");
		        
	        }while(kors[i] < 0 || 100 < kors[i]);
        
        System.out.println("|---------------------|");
    }
}
```



## 4. 매개변수를 이용한 함수 고립화

- 함수가 매개값을 하나도 안가지고 있었음
- 이는 함수가 외부의 변화에 영향을 받는다는 뜻임
  - 만약 누가 전역변수의 이름을 변경하면 이를 사용하던 함수들이 오작동하게 됨
- 독립적으로 고립시키는 게 좋음

![function_independent](Structured_JAVA_img/function_independent.png)



## 5. 함수 이름 짓기

- 숫자로 시작할 수 없다.
- 문자 사아에 빈 공백은 사용할 수 없다.
- 특수 문자는 사용할 수 없다.

### 예시 - 로또 생성 출력 정렬 프로그램

- 로또번호생성 => 생성로또번호 => genLotto()
- 로또번호출력 => 출력로또번호 => printLotto()
- 로또번호정렬 => 정렬로또번호 => sortLotto()

### 성적 출력 프로그램 리팩토링 결과

```java
package Part2.ex1.성적입력부분나누기;

import java.util.Scanner;

public class StructuredProgram{
	
    public static void main(String[] args) {
    	
    	int[] korList = new int[3];
        int menu;
        boolean keepLoop = true;			
        
		while(keepLoop)
		{
			menu = inputMenu();
	        
	        switch(menu) {	        
	        case 1:
	        	inputKors(korList);
		        break;
	        case 2:
		        printKors(korList);
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
    
    static void printKors(int[] kors) {
    	
    	int total = 0;
        float avg;
        
    	for(int i=0; i<3; i++)
        	total += kors[i];
        
        avg = total / 3.0f;
        
        System.out.println("|---------------------|");
		System.out.println("|      Score out      |");
		System.out.println("|---------------------|");
        System.out.println();		        
       
        for(int i=0;i<3;i++)
        	System.out.printf("국어%d : %3d\n", i+1, kors[i]);    	
        	        
        System.out.printf("총점 : %3d\n", total);
		System.out.printf("평균 : %6.2f\n", avg);
		System.out.println("|---------------------|");
    }
    
    static void inputKors(int[] kors) {
    	
    	Scanner scan = new Scanner(System.in);
    	int kor;
    	
    	System.out.println("|---------------------|");
		System.out.println("|       Score in      |");
		System.out.println("|---------------------|");
        System.out.println();
       		        
        for(int i=0; i<3; i++) {
	        do {
	        	System.out.printf("국어%d : ", i+1);
		        kor = scan.nextInt();
	        
		        if(kor < 0 || 100 < kor)
		        	System.out.println("out of scope 0~100");
		        
	        }while(kor < 0 || 100 < kor);
	        
	        kors[i] = kor;
        }
        
        System.out.println("|---------------------|");
    }
}
```



## 6. Top Down 방식으로 구현하는 간단 예제

### 로또 프로그램 분석

![Lotto_Program](Structured_JAVA_img/Lotto_Program.png)

```java
package Part2.ex2.탑다운예제;

public class Program {

	public static void main(String[] args) {
		
		int[][] lottos = null;
		int menu;
		boolean running = true;
		
		while (running) {
			
			menu = inputMenu();
			
			switch(menu) {
			case 1:
				lottos = createLottosAuto();
				break;
			case 2:
				lottos = createLottosManual();
				break;
			case 3:
				printLottos(lottos);
				break;
			case 4:
				running = false;
				break;
			default:
				
			}
		}

	}

	private static void printLottos(int[][] lottos) {
		
		
	}

	private static int[][] createLottosManual() {
		
		return null;
	}

	private static int[][] createLottosAuto() {
		
		return null;
	}

	private static int inputMenu() {
		
		return 0;
	}

}
```



## 7. 함수의 매개변수


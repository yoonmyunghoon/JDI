# Java Programming



## 1. 프로그래밍과 프로그래밍 언어

### 모든 버전의 공통분모인 자바 프로그래밍

- 자바 6, 7, 8, 9, .. 등 버전에 상관없이 자바 언어를 이용해서 절차를 만드는 방법을 배우는 것이 '자바 프로그래밍'
- JDK는 8버전 사용함
- 자바 프로그래밍
  - 자바를 이용해서 컴퓨터 프로그램을 만드는 방법
    - 자바 번역기(컴파일러)를 이용해서

### 동일한 프로그램이지만 방법을 달리 만들 수 있다.

- 자바 프로그래밍(절차 구현) < 구조적 프로그래밍 < 객체지향 프로그래밍
- 여기서는 절차적으로 프로그래밍하는 법을 먼저 배움



## 2. 번역기 준비하기

### 컴파일러 다운로드

- 두 가지 버전의 컴파일러

  - 오라클의 유료화된 JDK
  - OpenJDK

- JDK

  - Java Community Process에서 같이 만드는 것(오라클이 가장 큰 영향력이 있음, 삼성도 있음)
  - 새로운 기능이나 방법을 제안하고 누군가 요청하면 이때 실험적으로 만들어지는 것이 OpenJDK임

- OpenJDK

  - openJDK 8 버전 다운로드
  - 윈도우: https://github.com/ojdkbuild/ojdkbuild
  - 맥: https://github.com/AdoptOpenJDK/homebrew-openjdk

- JDK

  - bin
    - Javac.exe: 이게 컴파일러

- 환경변수 설정

  - mac의 Zsh에서 실행한 경우

  ```shell
  open ~/.zshrc
  
  여기서 path 추가해주고
  
  source ~/.zshrc
  
  적용하면 끝!
  ```

  - 윈도우에서는 시스템 환경변수설정에 들어가서 설정



## 3. 자바를 이용해서 컴퓨터 프로그램 만들기

### 자바 코드의 기본 규칙

- Program.java

```java
public class Program {
  public static void main(String[] args) {
    int a = 50;
    int b = 40;
    int c = 30;
    int tatal = a + b + c;

    System.out.printf("total is %d\n", total);
	}
}
```

```shell
// 컴파일러로 java파일을 컴파일
javac Program.java
// 컴파일하고나면 Program.class라는 파일이 생김

// 인터프리터로 실행(.class는 떼고)
java Program
```





## 4. 자바 IDE 이클립스 설치하기

### 통합개발환경(IDE)와 워크벤치(Work Bench)



## 5. 이클립스 사용하기




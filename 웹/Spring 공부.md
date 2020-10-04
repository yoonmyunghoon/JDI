# Spring Framework and Boot

![Spring](images/Spring.png)

## 1. 스프링 소개

### 스프링 프레임워크의 핵심 기능 : 기업용 애플리케이션을 만들 때 중요함

- Dependency Injection
- Transaction management
- 이 두가지 기능이 기업용 애플리케이션을 만들 때 중요함

### JAVA에는 세가지 종류가 있었음

- JAVA ME(모바일), SE(스탠다드), EE(엔터프라이즈)
- 이 중에서 Java EE가 기업용 애플리케이션 개발을 담당했었음
- 근데 위에서 말한 두가지 기능이 제공되기는 하지만 복잡했음
- 이 때 스프링이 나타나서 이 두가지 기능을 더 쉽고 깔끔하게 할 수 있게 해줌

### 기업형 응용 프로그램을 보조하기 위한 쉬운 프레임워크

- Java EE -> <b>Sprint</b>
  - 분산형, 기업형 응용 프로그램
  - 개발을 위한 API
  - 결합력을 낮추는 DI, DB Transaction 처리, 로그 처리...
- Java SE
  - 일반적인 로컬 응용 프로그램
  - 개발을 위한 API
  - 파일 I/O, 콘솔 I/O, 윈도우 I/O, 네트워크 I/O, Thread..
- 개발자들 생각
  - 기업용 애플리케이션을 만들고 있지만 EE는 안쓰는데? SE만 설치하고 개발하는데??
  - SE가 Spring으로 대체되었기 때문임

### 웹을 위한 스프링 프레임워크 모듈

![웹을 위한 스프링 프레임워크 모듈](images/웹을 위한 스프링 프레임워크 모듈.png)

- 아직까지 선택할 수는 있음
  - Java SE 위에 EE
  - Java SE 위에 Spring
  - Java SE 위에 EE + Spring
- 어찌되었건 웹 개발에 초점을 맞춘다면 크게 세가지 범주를 생각할 수 있음
  - MVC
    - DI
      - 느슨한 결합력과 인터페이스
  - 트랜잭션
    - DI, AOP
  - 인증과 권한
    - Servlet Filter
- 이전에 Java, SQL, MVC 등은 미리 알아둬야됨



## 2. 느슨한 결합력과 인터페이스







## 참고

- 유튜브 채널 - 뉴렉처
  - 스프링 프레임워크 강좌/강의
  - https://www.youtube.com/watch?v=XtXHIDnzS9c&list=PLq8wAnVUcTFUHYMzoV2RoFoY2HDTKru3T


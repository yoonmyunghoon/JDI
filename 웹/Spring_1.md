# Spring Framework and Boot 학습 1

![1](Spring_images/1.png)

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

- Java EE -> <b>Spring</b>으로 대체됨
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

![2](Spring_images/2.png)

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

### 코드 수정을 없애고 DI를 위한 설정

#### 어떤 레이어가 달라지면?

- 현재 상태

![3](Spring_images/3.png)

- B1의 수정이 필요함
  - B1의 소스코드를 구해서 수정한다? 재배포를 해야함.. 안좋은 방법임
  - B1은 그대로 두고, B2를 만들어서 덮어쓰기한다?
    - 이렇게 한다고해도 S를 수정해줘야함
    - 결합력이 높은 상태임

![4](Spring_images/4.png)

- 덮어쓰기를 하되, 수정하는 부분을 최소화하자
  - 소스코드없이 바꾸게 만들자 == 결합력을 낮추자
  - B라는 인터페이스를 사용하자
    - 참조형식 부분은 수정을 안해도 되도록 만들었음
  - 이제 객체타입도 B2로 바꿔야하는데 어떻게할 수 있을까?

![5](Spring_images/5.png)

- 객체타입을 변경해서 갈아끼우는 작업을 UI에서 해주자
  - 소스코드 수정없이 가능하게 하기 위해서는 외부파일이나 외부설정을 사용해야함
  - 객체를 생성하는 부분을 비워두고, 외부파일이나 외부설정을 통해 변경될 수 있도록 만들자
  - 자바 객체지향 강의 33강 참고하기
    - https://www.youtube.com/watch?v=YZzpGtpW2h0&list=PLq8wAnVUcTFV4ZjRbyGnw6T1tgmYDLM3P&index=87

![6](Spring_images/6.png)

#### 결론

- 기업형 어플리테이션을 만들 때 다양한 레이어를 만들게 되고, 이것을 유지보수하게 됨
- 매번 소스코드를 열어서 수정하고 재배포하는 식의 유지보수는 위험부담이 있음
- 그래서 소스코드를 수정하는 방식보다는 대체하거나 추가하는 방식으로 유지보수를 하게 됨
- 그러기 위해서는 인터페이스와 설정파일이 필요함
  - 결합력을 낮추기 위한 방법임
- 스프링이 이런 것들을 도와줌
  - 결합할 때 필요한 설정파일을 제공
  - 객체를 결합해주는 역할을 함



## 3. DI(Dependency Injection)

### 스프링 프레임워크

#### 스프링 프레임워크 코어 기능: 종속 객체를 생성, 조립해주는 도구

- 스프링이 가지고 있는 가장 기본적인 능력은 무엇인가?
  - 객체를 생성해주고, 객체들을 조립해주는 능력
    - DI(Dependency Injection)
    - IoC Container

### Dependency들을 조립하기 - Dependecy를 부품으로 생각해보자

- Composition has a
  - 일체형
  - A가 생성될 떄, 부품인 B도 함께 생성됨
- Association has a
  - 조립형
  - A가 생성되더라도 B가 생성되지 않음
  - B는 외부에서 생성됨
  - 외부에서 생성된 객체를 셋팅해서 사용할 수 있음

![7](Spring_images/7.png)

### DI(Dependency Injection)

#### Dependency

- 일체형보다는 조립형이 결합력을 낮춰주고, 부품을 쉽게 갈아끼울 수 있는 형태임
- 그래서 유지보수나 업데이트 등을 고려하는 기업형 어플리케이션에서는 조립형으로 많이 만듬
- Dependecy Injection을 사용했을 경우
  - 장점: 부품을 쉽게 바꿀 수 있음
  - 단점: 부품을 조립해야하는 번거로움이 있음
    - 누군가 부품을 대신 조립해주면 좋을텐데..
    - Spring이 그 역할을 해줌

![8](Spring_images/8.png)

#### Injection - 조립하는 방법 두가지

- Setter Injection
- Construction Injection

![9](Spring_images/9.png)

- 스프링은 객체 생성과 조립을 해줌
- 부품을 조립해주는 것이 Dependency Injection임
  - 원하는 부품들이 어떤것이 있고, 어떤 부품 결합을 하길 원하는지 설정을 해주면 스프링이 그런일을 해줌
  - 우리는 조립된 결과물을 가져다 쓰면 됨
- 객체를 조립해주기 위해서는 컨테이너가 필요한데, 그게 IoC Container임



## 4. IoC(Inversion of Control) 컨테이너

### DI(Dependency Injection)

- 부품을 조립해주는 능력
- 여러가지 부품들을 주문서에 적어서 스프링에게 제공해주어야함
- 스프링은 주문서를 보고 부품(객체)을 생성하고 조립함
- 어떤 부품이 필요하고 어떤 조립관계를 가져야하는지 명세화할 수 있어야함 - 두가지 방법
  - XML 파일
  - Annotation
- 주문서에 맞게 부품을 생성해서 담을 수 있는 공간이 필요함
  - IoC Container

![10](Spring_images/10.png)

### IoC(Inversion of Control) Container

- 왜 IoC라는 이름이 붙었나?
- 일체형의 경우, 큰 것이 조립되면 하위 부품들이 조립되는 순서
- 조립형의 경우, 작은 것부터 조립되고, 점점 커지는 순서
  - 조립까지해준다는 의미가 포함되어서, 순서가 역순이라는 의미로 IoC가 붙음

#### DI 순서

![11](Spring_images/11.png)



## 5. Dependecy를 직접 Injection하기





## 참고

- 유튜브 채널 - 뉴렉처
  - 스프링 프레임워크 강좌/강의
  - https://www.youtube.com/watch?v=XtXHIDnzS9c&list=PLq8wAnVUcTFUHYMzoV2RoFoY2HDTKru3T


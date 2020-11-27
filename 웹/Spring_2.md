# Spring Framework and Boot 학습 2

![1](Spring_images/1.png)



## 11. 콜렉션 생성과 목록 DI

- 콜렉션 생성과 콜렉션에 객체를 참조시키는 초기화 작업을 어떻게 DI할 것인가 알아보자
- Program.java

```java
package spring.di;

import java.util.ArrayList;
import java.util.List;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import spring.di.entity.Exam;
import spring.di.entity.NewlecExam;
import spring.di.ui.ExamConsole;
import spring.di.ui.GridExamConsole;
import spring.di.ui.InlineExamConsole;

public class Program {

	public static void main(String[] args) {
		
		ApplicationContext context = 
				new ClassPathXmlApplicationContext("spring/di/setting.xml");
		
		Exam exam = context.getBean(Exam.class);
		System.out.println(exam.toString());
		
		ExamConsole console = context.getBean(ExamConsole.class);
		console.print();
		
    // List 생성
		List<Exam> exams = (List<Exam>) context.getBean("exams"); //new ArrayList<>();
    // List에 객체 추가
//		exams.add(new NewlecExam(1,1,1,1));
		
		for(Exam e : exams) {
			System.out.println(e);
		}
	}
}

```

- setting.xml
- namespace를 사용하지 않은 방법

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-4.3.xsd">
	<bean id="exam" class="spring.di.entity.NewlecExam" p:kor="10" p:eng="10" />
	<bean id="console" class="spring.di.ui.InlineExamConsole">
		<property name="exam" ref="exam" />
	</bean>
	
  <!-- ArrayList 객체 생성, 생성자로 collection을 넘기는 방식 -->
	<bean id="exams" class="java.util.ArrayList">
		<constructor-arg>
			<list>
        <!-- id는 따로 안적음 -->
				<bean class="spring.di.entity.NewlecExam" p:kor="1" p:eng="1" />
        <!-- 이렇게 id로 참조하는 방법도 있음 -->
				<ref bean="exam"/>
			</list>
		</constructor-arg>
	</bean> 
	
</beans>

```

- namespace를 사용하는 방법
  - xmlns:util 사용

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:util="http://www.springframework.org/schema/util"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-4.3.xsd">
	<bean id="exam" class="spring.di.entity.NewlecExam" p:kor="10" p:eng="10" />
	<bean id="console" class="spring.di.ui.InlineExamConsole">
		<property name="exam" ref="exam" />
	</bean>
	<!-- namespace를 사용-->
	<util:list id="exams" list-class="java.util.ArrayList">
		<bean class="spring.di.entity.NewlecExam" p:kor="1" p:eng="1" />
		<ref bean="exam"/>
	</util:list>
	
</beans>

```



## 12. 어노테이션을 이용할 때의 장점과 @Autowired를 이용한 DI 해보기

- 어플리케이션을 만들 때, 초기화 설정을 만드는 방법에는 두가지가 있음
  - 첫번째
    - xml을 사용해서 외부에 설정정보를 두는 방법
  - 두번째
    - 어노테이션이라는 방법으로, 코드파일에 설정정보를 심는 방법
    - 코드파일에 심은 설정정보를 어노테이션이라고 함
- 어노테이션을 이용했을 때의 장점에 대해 알아보고 DI하는 부분을 어노테이션으로 바꿔보자

### 스프링 어노테이션

![26](Spring_images/26.png)

### Annotation으로 설정할 때의 장점

#### XML로 설정할 때의 모듈 변경 방법

- 외부파일을 통해 B2를 DI했음

![27](Spring_images/27.png)

- B3로 대체해야하는 상황

![28](Spring_images/28.png)

- 외부파일을 수정해주어야함
  - 외부파일을 수정해주는 작업도 없애고 싶어서 어노테이션이 나옴

![29](Spring_images/29.png)

#### Annotation으로 설정할 때의 모듈 변경 방법

- B2 클래스 코드에 @Component라는 어노테이션을 달아두면 스프링이 읽고 객체로 만들어줌

![30](Spring_images/30.png)

- B2를 없애고, B3에 어노테이션을 달고 도킹해주는 어노테이션(@Autowired)까지 달면 대체가 됨
  - 다른 외부파일을 손대거나 할 필요가 없어짐

![31](Spring_images/31.png)

### DI 지원을 위한 스프링 어노테이션

#### @Autowired 어노테이션

![32](Spring_images/32.png)

![33](Spring_images/33.png)

- Program.java

```java
package spring.di;

import java.util.ArrayList;
import java.util.List;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import spring.di.entity.Exam;
import spring.di.entity.NewlecExam;
import spring.di.ui.ExamConsole;
import spring.di.ui.GridExamConsole;
import spring.di.ui.InlineExamConsole;

public class Program {

	public static void main(String[] args) {
		
		ApplicationContext context = 
				new ClassPathXmlApplicationContext("spring/di/setting.xml");
		
		ExamConsole console = context.getBean(ExamConsole.class);
		console.print();
	}
}
```

- setting.xml
  - console에 exam을 DI하는 부분 없앰
  - 스프링이 이 파일을 읽다가 객체를 생성하면 그 클래스로 가서 @Autowired가 있는지 확인할 수 있도록 namespace사용
    - xmlns:context
    - <context:annotation-config /> 추가

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:util="http://www.springframework.org/schema/util"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd
		http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-4.3.xsd">
	
	<context:annotation-config />
	<bean id="exam" class="spring.di.entity.NewlecExam" p:kor="10" p:eng="10" />
	<bean id="console" class="spring.di.ui.InlineExamConsole">
		<!-- <property name="exam" ref="exam" /> -->
	</bean>
	
	<util:list id="exams" list-class="java.util.ArrayList">
		<bean class="spring.di.entity.NewlecExam" p:kor="1" p:eng="1" />
		<ref bean="exam"/>
	</util:list>
	
</beans>

```

- InlineExamConsole.java
  - setExam에 @Autowired 달아주기
  - 그런데 어노테이션을 달아주기만 했을 뿐인데 넘겨지는 값에 대한 정보는 어떻게 알아서 처리해주는 건가?

```java
package spring.di.ui;

import org.springframework.beans.factory.annotation.Autowired;

import spring.di.entity.Exam;

public class InlineExamConsole implements ExamConsole {
	
	private Exam exam;
	
	public InlineExamConsole() {
	}
	
	public InlineExamConsole(Exam exam) {
		this.exam = exam;
	}

	@Override
	public void print() {
		System.out.printf("total is %d, avg is %f\n", exam.total(), exam.avg());

	}

	@Autowired
	@Override
	public void setExam(Exam exam) {
		this.exam = exam;
		
	}

}

```



## 13. @Autowired의 동작방식 이해와 @Qualifier 사용하기

### 객체 생성과 Autowired

- xml에서 객체를 생성하고 Autowired를 사용해서 DI도 해줬음
- 그런데 어떤 객체와 DI해야하는지를 어떻게 스프링이 알아서 해주는건가?

![34](Spring_images/34.png)

- InlineExamConsole.java
  - 기본적으로 매개변수로 들어오는 객체의 자료형에 맞춰서 받아옴
  - 여기서는 Exam 타입이기 때문에 이 인터페이스를 상속하는 NewlecExam 객체를 받아옴

```java
@Autowired
@Override
public void setExam(Exam exam) {
  this.exam = exam;

}
```

- NewlecExam객체가 한 개인 setting.xml
  - 객체의 타입으로 가져오는 것이기 때문에 id값이 다르거나 없어도 인식할 수 있음
  - 단, 똑같은 타입의 객체가 여러개라면 오류가 발생함

```xml
<bean id="exam1" class="spring.di.entity.NewlecExam" p:kor="10" p:eng="10" />
```

- NewlecExam객체가 여러개인 setting.xml
  - 이 경우에는 매개변수명으로 찾아올 수 있음

```xml
<bean id="exam" class="spring.di.entity.NewlecExam" p:kor="10" p:eng="10" />
<bean id="exam1" class="spring.di.entity.NewlecExam" p:kor="20" p:eng="20" />
```

- 그런데 이렇게 이름이 전부 틀릴 경우에는 어떻게 해야하나?
  - setter의 매개변수명을 변경하는 것은 바람직하지 않음
  - @Qualifier 어노테이션을 사용해야함

```xml
<bean id="exam1" class="spring.di.entity.NewlecExam" p:kor="10" p:eng="10" />
<bean id="exam2" class="spring.di.entity.NewlecExam" p:kor="20" p:eng="20" />
```

- InlineExamConsole.java

```java
@Autowired
@Qualifier("exam2")
@Override
public void setExam(Exam exam) {
  this.exam = exam;

}
```

### 정리

- 자료형식을 기본으로하되, 식별이 모호할 경우에는 자료명도 사용함
- 자료명에 맞춰서 매개변수명을 바꾸는건 바람직하지 않음
- @Qualifier를 사용해서 식별할 수 있도록 하자



## 14. @Autowired의 위치와 Required 옵션









## 참고

- 유튜브 채널 - 뉴렉처
  - 스프링 프레임워크 강좌/강의
  - https://www.youtube.com/watch?v=XtXHIDnzS9c&list=PLq8wAnVUcTFUHYMzoV2RoFoY2HDTKru3T


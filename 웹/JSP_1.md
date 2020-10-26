# JSP 학습 1

> 'Servlet'에 이어서 'JSP'를 학습해보자



## 40. JSP 시작하기(Jasper를 이용한 서블릿 프로그래밍)

### JSP를 이용한 자바 웹 프로그래밍

- Jasper라는 소프트웨어를 통해 서블릿을 좀 더 쉽게 개발할 수 있다
- Jasper를 이용한 서블릿 프로그램
- 이를 JSP 프로그램이라고 함
- 왜 Jasper를 사용해야하는지, 이로 인해 얻을 수 있는 이점은 무엇인지 알아보자

### HTML 출력이 많은 결과 페이지

- 간단한 문자를 몇 개 보내주는 거라면 Jasper를 사용할 필요가 없음
- 하지만, 대부분의 웹 페이지는 복잡한 html으로 구성되어있음

![1](JSP_images/1.png)

### 서블릿 출력 코드에서 HTML을 출력하는 방법

- 서블릿 내에서 구현하려면 전부 코드로 직접 써줘야 됨
- 이런 번거로운 작업을 줄이자해서 만들어진게 자바쪽에서는 Jasper임

![2](JSP_images/2.png)

### Jasper가 만들어주는 서블릿 출력 코드

- Jasper한테 이런 html코드들 앞에 out.write()를 다 붙혀서 서블릿코드를 만들어달라고 함
- 어떻게 만드는가?
  - add.jsp
  - jsp라는 확장자를 붙여줌
  - 이렇게하면 여기에 있는 내용들을 다 출력해야햐는 것으로 인식하고 출력할 수 있는 형태로 바꿔줌
- 언제 바꿔주나?
  - add.jsp를 언제 서블릿 코드로 바꿔주는가?
  - 사용자가 이 add.jsp 페이지를 요청할 때 만들어짐
  - URL 매핑은 이 파일이름(확장자까지 포함된, add.jsp)이 됨

![3](JSP_images/3.png)

- 실제로 만들어진 서블릿 코드의 이름은 add_jsp.java
  - server탭에 있는 서버를 더블클릭하거나 오른쪽을 클릭해서 open을 누르면
  - 서버 설정에 대한 내용이 나옴
  - 이클립스를 통해 코드를 수정하고 파일을 생성하고 하지만, 실제로 브라우저는 우리가 보고있는 부분을 보는게 아님
    - 우리가 코드를 고치고 생성하고 하는 부분은 개발 디렉토리임
    - 이걸 실행하면 배포를 하게 됨
    - 배포하게 되면 tomcat의 홈디렉토리로 옮겨지게 됨
    - 그런데 사용하고 있는 tomcat이 다른 서비스도 운영하고 있을 수도 있기 때문에
    - 실제 톰캣의 work 디렉토리에 두지 않고, 이클립스가 관리하는 별도의 운영을 위한 복사본을 만들게 됨
    - Server Location 부분에 있는 Server Path가 임시 배포 디렉토리임
    -  ..../Servlet_JSP/workspace/.metadata/.plugins/org.eclipse.wst.server.core
    - 여기서 더 들어가면
    - tmp0/work/Catalina/localhost/ROOT/org/apache/jsp/calculator_jsp.java
      - work는 jasper가 일하는 공간
      - jasper가 만들어낸 파일들이 있음
- calculator_jsp.java을 열어서 보면
  - 이렇게 다 out.write()를 다 붙여줬음

![4](JSP_images/4.png)

### Jasper를 이용한 코드 작성 방법

- 만약 jsp파일에서 변수를 선언하고 싶다고하면 어떻게해야할까?
  - 출력하기를 원하는게 아니라 서블릿 내에서 동작할 수 있도록 변수를 선언하고 싶은 것임
  - 이렇게 한다고하면 될까? X
  - 아무런 표시없이 적어주면 Jasper는 코드로 인식을 못함
  - 그냥 write를 붙여줘버림

![5](JSP_images/5.png)

- 코드 블록을 사용해야함
  - 이게 서블릿을 Jasper를 통해서 만드는 방법임
  - 앞으로 이런 코드 블록을 어떻게 이용하는지, 코드 블록의 종류가 몇가지인지, 어떻게하면 잘 활용하는 것인지 등을 공부할 것임

![6](JSP_images/6.png)

- calculator.jsp

```jsp
<%
int x = 3;
int y = 4;
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
	input{
		width:50px;
		height:50px;
	}
	.output{
		height:50px;
		background: #e9e9e9;
		font-size: 24px;
		font-weight: bold;
		text-align: right;
		padding: 0px 5px;
	}
</style>

<title>calculator</title>
</head>
<body>
	<div>
		<form action="calc3" method="post">
			<table>
				<tr>
					<td class="output" colspan="4">${3+4}</td>
				</tr>
				<tr>
					<td><input type="submit" name="operator" value="CE" /></td>
					<td><input type="submit" name="operator" value="C" /></td>
					<td><input type="submit" name="operator" value="BS" /></td>
					<td><input type="submit" name="operator" value="/" /></td>
				</tr>
				<tr>
					<td><input type="submit" name="value" value="7" /></td>
					<td><input type="submit" name="value" value="8" /></td>
					<td><input type="submit" name="value" value="9" /></td>
					<td><input type="submit" name="operator" value="*" /></td>
				</tr>
				<tr>
					<td><input type="submit" name="value" value="4" /></td>
					<td><input type="submit" name="value" value="5" /></td>
					<td><input type="submit" name="value" value="6" /></td>
					<td><input type="submit" name="operator" value="-" /></td>
				</tr>
				<tr>
					<td><input type="submit" name="value" value="1" /></td>
					<td><input type="submit" name="value" value="2" /></td>
					<td><input type="submit" name="value" value="3" /></td>
					<td><input type="submit" name="operator" value="+" /></td>
				</tr>
				<tr>
					<td></td>
					<td><input type="submit" name="value" value="0" /></td>
					<td><input type="submit" name="dot" value="." /></td>
					<td><input type="submit" name="operator" value="=" /></td>
				</tr>
			</table>
		</form>
	</div>
</body>
</html>
```



## 41. JSP의 코드 블록

- Jasper를 통해 간접적으로 서블릿을 만들 때, 자바 코드를 끼워넣고 싶다면, 코드 블록을 사용해야함
- 몇가지 코드 블록 지시방법에 대해 알아보자

### 코드 블록의 종류1 : 출력 코드

- 아무것도 안했을 경우
- 출력하게 됨

![7](JSP_images/7.png)

### 코드 블록의 종류2 : 코드 블록

- 코드 블록을 사용
- 자바 코드로 들어가게 됨 

![8](JSP_images/8.png)

### 코드 블록의 종류3 : 코드 블록

- 출력을 하되, 선언했던 변수도 함께 출력하고 싶은 경우
- 코드 블록안에 out.print()를 사용해서 출력하는 자바 코드를 넣어줌

![9](JSP_images/9.png)

- 이때, 변수 출력을 위해서 코드 블록안에 출력문을 일일히 넣어주는 것은 번거롭기 때문에 다음과 같은 방식을 사용할 수 있음
  - <%= 변수 %>
  - 이런식으로 표현하면 위의 방법과 동일한 결과가 나옴

![10](JSP_images/10.png)

### 코드 블록의 종류 4 : 선언부(Declaration)

- service함수 안이 아니라 밖에, 클래스의 멤버함수와 멤버변수로써 선언하고자할 때
- <%! 자바 코드 %>

![11](JSP_images/11.png)

### 코드 블록의 종류5 : 초기 설정을 위한 Page 지시자

- 자바 코드가 아니라 페이지에 대한 정보를 나타내고 있음
  - key와 value로 나타내어진 데이터임
  - 어떤 형태의 인코딩 방식을 사용할 것인지, 컨텐트 타입은 무엇인지 등을 지시하는 것
- 이는 코드 블록이라고하지 않고 Page 지시자 블록이라고 함

![12](JSP_images/12.png)

- 왜 이런 지시 블록이 필요한가?
  - 과거에는 response를 사용하기 전에 이런것들을 써줘서 인코딩 설정을 해줬었음
  - response.setCharacterEncoding("UTF-8");
  - response.setContentType("text/html; charser=UTF-8");
  - 이를 코드 블록으로 할 수 있지 않나?
    - 이렇게 하면 에러가 나옴
      - 이미 출력이 진행된 다음에 설정하는 것은 잘못된 것이다라는 오류
      - 이 코드 블록이 실행되기전에 위쪽에서 하나라도 출력되는 부분이 있다는 말임
      - 그래서 어쩔 수 없이 코드 지시자를 써야함

![13](JSP_images/13.png)



## 42. JSP의 내장객체 간단히 알아보기

### 코드 블록의 내장 객체

- jsp로 코드를 작성하며 Jasper가 서블릿을 만들어주는데 이때 고려해야되는 부분이 있음
- 내가 jsp파일에 작성한 코드뿐만아니라 Jasper가 만든 서블릿에도 자동으로 만들어진 코드가 존재한다는 것
- 다음과 같이 page라는 변수를 선언했을 때 오류가 발생하는 것은 이미 서블릿의 service함수에 page라는 이름의 변수가 존재하기 때문임
- 그래서 jsp를 사용하려면 자동 생성되는 서블릿의 코드를 좀 알아야됨

![14](JSP_images/14.png)

### JSP 내장 객체

- jasper에 의해 자동으로 만들어진 변수들은 다 객체를 가리키는 변수들임
- 이런 변수들을 내장 객체라고 함
- 이런 변수들이 있다는 것을 미리 알고 있어야 중복된 이름의 변수를 만들지 않을 뿐더러 jsp의 코드블록에서 이들을 적절히 활용해서 프로그램을 만들 수 있음
- 대표적으로 request, response가 있음
- application, session 객체
- pageContext
  - 페이지 내에서 임시로 데이터를 저장할 수 있도록하 객체
  - setAttribute, getAttribute를 가지고 있음
  - application, session이 전역적으로 사용되는 데이터를 가지고 있다면 pageContext는 이 페이지 내에서만 사용되는 저장소
- config
- out
  - 출력 도구
- page
  - 페이지 자체의 객체를 참조하는 변수

![15](JSP_images/15.png)

### 내장 객체 request : HttpServletRequest

- 요청을 확인하고 입력을 하기 위한 도구
- 사용자가 전달한 파라미터 관련 정보, 쿠키, 요청 방식, 세션, 사용자의 IP주소, 문자셋 인코딩 설정, 헤더 정보, 쿼리 스트링 등을 알 수 있음

![16](JSP_images/16.png) 

### 내장 객체 response : HttpServletResponse

- 응답으로 보낸 때, 출력할 도구
- 쿠키 입력, redirect, 헤더정보 입력, 컨텐트 타입 입력, 상태 코드 설정 등을 할 수 있음

![17](JSP_images/17.png)

### 내장 객체 out : Java.servlet.jsp.JspWriter

- 출력할 때 사용하는 객체
- 직접 쓰는 일은 많지 않음
- 쓸 수 있지만 안씀
- 이미 jasper를 쓰고 있기 때문에 직접 out.write를 사용하는 일은 지양해야됨

![18](JSP_images/18.png)

### 내장 객체 session : javax.servlet.http.HttpSession

- 생성 일자, 마지막 액세스 시간 등을 알 수 있음
- 가장 중요한 기능은 값을 설정하고 얻어낼 수 있고, 값이 저장되는 시간을 설정하고, 특정값을 삭제하는 기능 등임

![19](JSP_images/19.png)

### 내장 객체 application : javax.servlet.ServletContext

- 서블릿들이 공통으로 사용할 수 있는 전역 저장소

![20](JSP_images/20.png)



## 43. JSP로 만드는 Hello 서블릿

- nana.jsp
  - 이전에 만들었던 Nana.java(서블릿)을 jsp로 만들어보자

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%
String cnt_ = request.getParameter("cnt");

int cnt = 10;

if(cnt_ != null && !cnt_.equals("")) {
	cnt = Integer.parseInt(cnt_);
}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%for(int i=0; i<cnt; i++){ %>
		안녕 Servlet!!<br >
	<%} %>
</body>
</html>
```

![21](JSP_images/21.png)



## 44. 스파게티 코드를 만드는 JSP

- JSP를 만드는 방법이 너무 다양해서 페이지를 만들다보면 간단하게 만들 수도 있지만, 복잡하게 만들 수도 있음
- 복잡하게 만들었을 경우, 그 코드를 스파게티 코드라고 하는데 그게 왜 문제가 되는지 알아보자
- 그 다음에는 스파게티 코드를 개선할 수 있는 방법에 대해 알아보자
- 일단 간단한 jsp 파일을 하나 추가해보자
- spag.jsp
  - 코드 블록을 여러 군데 순서만 맞도록해서 쓰면 오류가 나지 않음
  - 하지만, 여러 군데 코드 블록을 써서 코드를 짜다보면 다른 오류를 찾는 것이 어려워짐
  - 자바 코드를 보기가 어려워짐
  - 어떤 블록과 어떤 블록이 단일한 업무를 다루고 있는지 찾기가 쉽지 않음
  - 이런 스파게티 코드, 실타래 코드를 어떻게 하면 개선할 수 있을까?
  - 코드를 한곳에 모아서 쉽게 유지보수할 수 있는 방법을 알아보자

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<% int num = 0; %>
<!DOCTYPE html>
<html> 
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<%
	String num_ = request.getParameter("n");
	if(num_ != null && !num_.equals("")) {
		num = Integer.parseInt(num_);
	}
%>
<body>
	<% if(num%2 != 0) { %>
		홀수입니다.
	<% } else {%>
		짝수입니다.
	<% } %>
</body>
</html>
```











## 참고

- 유튜브 채널 뉴렉처








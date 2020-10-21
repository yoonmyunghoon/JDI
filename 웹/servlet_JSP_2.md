# 서블릿/JSP Study



## 16. 기본 값 사용하기

- 사용자가 입력값을 따로 안줘도 오류가 안나려면 기본값이 필요

### 전달되는 입력 값의 형태

#### 쿼리스트링을 다음처럼 사용할 경우에 전달 되는 int 값은...?

![28](servlet_JSP_images/28.png)

#### 전달 방식의 차이

- null이나 빈 문자열일 경우에는 기본값으로 대체

![29](servlet_JSP_images/29.png)

- 코드 업데이트

```java
package com.reynold.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hi")
public class Nana extends HttpServlet {
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		
		PrintWriter out = response.getWriter();
		
		String cnt_ = request.getParameter("cnt");
		
		int cnt = 100;
		
		if(cnt_ != null && !cnt_.equals("")) {
			cnt = Integer.parseInt(cnt_);
		}
		
		for(int i=0; i<cnt; i++) {
			out.println((i+1) + "번째 줄 : 안녕 Servlet<br />");
		}
		
	}
}

```

- 그런데 이러한 값들을 사용자가 항상 주소창으로 전달할까? No
  - Index.html에서 하이퍼텍스트를 통해서 주소로 접근할 수 있도록 하자
  - a 태그를 사용하자

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	환영합니다.<br >
	<a href="hi">인사하기</a><br >
	<a href="hi?cnt=3">인사하기</a><br >
</body>
</html>
```



## 17. 사용자 입력을 통한 GET 요청

- 사용자가 직접 입력시킬 수 있도록 해보자

### 반복횟수를 사용자로부터 입력 받으려면 입력폼을 준비해야된다.

![30](servlet_JSP_images/30.png)

### 입력 폼

- form 태그와 input 태그를 사용하자
  - form 태그의 action을 통해 매핑 주소를 입력해주자
  - input 태그를 통해 입력값을 받을 수 있도록 name을 맞춰주자
  - form과 input 태그를 사용하면 브라우저가 저런식으로 주소를 만들어서 요청을 보내줌

![31](servlet_JSP_images/31.png)

- hello.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<div>
		<form action="hi">
			<div>
				<label>"안녕하세요"를 몇 번 듣고 싶으세요?</label>
			</div>
			<div>
				<input type="text" name="cnt" />
				<input type="submit" value="출력" />
			</div>
		</form>
	</div>
</body>
</html>
```



## 18. 입력할 내용이 많은 경우는 POST 요청

### POST 요청의 일반적인 요청 방식

#### 요청과 제출, 두 단계로 나누어서 일을 처리하려고 할 때의 두 가지 요청

- 입력 폼을 받기위해서 GET 요청
- 받은 입력 폼을 작성해서 POST 요청

![32](servlet_JSP_images/32.png)

### title과 content를 보내는 POST 요청을 만들어보자

- reg.html
  - title과 content를 입력할 수 있는 form을 제공
  - post 방식으로 notice-reg로 보냄

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<div>
		<form action="notice-reg" method="post">
			<div>
				<label>제목:</label><input name="title" type="text" >
			</div>
			<div>
				<label>내용:</label>
				<textarea name="content"></textarea>
			</div>
			<div>
				<input type="submit" value="등록" />
			</div>
		</form>
	</div>
</body>
</html>
```

- NoticeReg.java
  - notice-reg를 매핑받아서 처리를 담당할 서블릿을 작성하자
  - title과 content를 받아서 그대로 보여주는 기능을 구현

```java
package com.reynold.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/notice-reg")
public class NoticeReg extends HttpServlet {
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		
		PrintWriter out = response.getWriter();
		
		String title = request.getParameter("title");
		String content = request.getParameter("content");
		
		out.println(title);
		out.println(content);
		
		
	}
}

```

- 영어로 입력했을 경우, 잘나오지만 한글을 입력했을 경우 이상한 문자가 결과로 보여짐



## 19. 한글 입력 문제

### 한글이 전달되는 것을 서버에서 받지 못하는 문제

#### 멀티 바이트 문자 전송 문제: 사용자로부터 값 입력 받아서 전송하기

- 영문자는 문자하나당 숫자로 변환될 때 1바이트지만, 한글은 2바이트를 사용해야 제대로 표현할 수 있음
- 보낼 때는 잘 보냈는데 웹 서버에서 2바이트씩 UTF-8 방식으로 읽으면 제대로 읽히지만, 그렇지 않은 경우에는 이상한 문자로 해석하게 됨
- 그런데 사용하고 있는 웹서버(아파치 톰캣)은 ISO-8859-1 인코딩 방식을 사용하고 있음
  - 1바이트를 한 문자로 인식하고 있음
  - 한글이 깨짐
  - 깨진 값을 다시 보내니까 이상하게 보여지는 것

![33](servlet_JSP_images/33.png)

- 이를 해결할 수 있는 방법 2가지
  - request.setCharacterEncoding("UTF-8"); 을 사용해서 요청을 받을 때 인코딩 변환해줘서 받기
  - 톰캣의 환경설정인 server.xml의 Connector 부분에 UTF-8로 인코딩할 수 있도록 코드 추가해주기
    - 그런데 일반적으로 톰캣 서버의 환경설정은 잘 안건드림
      - 만약 톰캣에서 여러개의 서비스를 돌릴 경우, 다른 서비스들도 영향을 줄 수 있기 때문에

![34](servlet_JSP_images/34.png)

- NoticeReg.java

```java
package com.reynold.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/notice-reg")
public class NoticeReg extends HttpServlet {
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
    // 추가
		request.setCharacterEncoding("UTF-8");
		
		PrintWriter out = response.getWriter();
		
		String title = request.getParameter("title");
		String content = request.getParameter("content");
		
		out.println(title);
		out.println(content);
	}
}
```



## 20. 서블릿 필터(Servlet Filter)

### 필터

- 웹 서버 <-> WAS <-> Servlet Container
- 웹 서버가 정적 요청 담당하고 동적인 부분은 WAS에게 넘김
- WAS(톰캣)가 사용자로부터 요청을 받으면 적절한 소프트웨어를 실행해서 결과를 돌려주게 되어있음
- 이 소프트웨어가 서블릿이고 서블릿이 실행될 때 메모리에 존재하게 되는데, 이때의 공간이 Sevlet Container임
- WAS는 서블릿을 실행시켜서 결과를 Servlet Container에 넣어뒀다가 돌려줌
- 더이상 서블릿이 사용되지 않으면 Servlet Container에서 삭제함

![35](servlet_JSP_images/35.png)

- 그런데 서블릿 말고 만들 수 있는 객체가 하나 더 있음
- 그게 필터임
  - 필터는 WAS와 Sevlet Container 사이에 있음
  - 요청과 응답 과정에서 가로채서 먼가 더 처리를 해줄 수 있음
  - 요청을 먼저 받아서 서블릿을 실행할 것인지 말것인지를 검사하고 제어할 수 있음
    - 인증과 권한 기능을 구현할 때 사용됨
      - 수문장의 역할
    - 모든 서블릿이 사용해야되는 기본 기능을 여기서 구현할 수도 있음
      - 예를 들어 한글을 입력 받는 서블릿을 만들면 인코딩을 해줘야함
      - request.setCharacterEncoding("UTF-8"); 이 코드를 각 서블릿마다 작성해줘야함
      - 그런데 모든 서블릿에서 이 코드를 작성하는 것이 아니라 필터에서 이런 부분을 담당할 수 있음
  - 실행되고 응답하는 과정에서도 먼가 추가적인 작업을 해줄 수 있음

![36](servlet_JSP_images/36.png)

- filter를 만들고 설정해줘야됨. 방법 2가지

  - web.xml에서 코드를 통한 설정

    - CharacterEncodingFilter.java

    ```java
    package com.reynold.web.filter;
    
    import java.io.IOException;
    
    import javax.servlet.Filter;
    import javax.servlet.FilterChain;
    import javax.servlet.ServletException;
    import javax.servlet.ServletRequest;
    import javax.servlet.ServletResponse;
    import javax.servlet.annotation.WebFilter;
    
    public class CharacterEncodingFilter implements Filter {
    
    	@Override
    	public void doFilter(ServletRequest request, 
    			ServletResponse response, 
    			FilterChain chain)
    			throws IOException, ServletException {
    
    //		System.out.println("before filter");
    		
        // 다음으로 가기 전에 인코딩 설정해줌
    		request.setCharacterEncoding("UTF-8");
    		
        // 이 코드가 중요
        // 이 코드 위쪽은 다음으로 가기 전에 실행되고, 이 코드 밑쪽은 응답하고 나서 실행됨
    		chain.doFilter(request, response);
    		
    //		System.out.println("after filter");
    
    	}
    
    }
    ```

    - web.xml
      - servlet 설정해준거랑 비슷

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                          http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
      version="4.0"
      metadata-complete="false">
      
      <filter>
      	 <filter-name>characterEncodingFilter</filter-name>
      	 <filter-class>com.reynold.web.filter.CharacterEncodingFilter</filter-class>
      </filter>
      <filter-mapping>
      	 <filter-name>characterEncodingFilter</filter-name>
      	 <url-pattern>/*</url-pattern>
      </filter-mapping>
    
      <display-name>Welcome to Tomcat</display-name>
      <description>
         Welcome to Tomcat
      </description>
    
    
    </web-app>
    
    
    
    ```

  - 어노테이션 방법

    - CharacterEncodingFilter.java

    ```java
    package com.reynold.web.filter;
    
    import java.io.IOException;
    
    import javax.servlet.Filter;
    import javax.servlet.FilterChain;
    import javax.servlet.ServletException;
    import javax.servlet.ServletRequest;
    import javax.servlet.ServletResponse;
    import javax.servlet.annotation.WebFilter;
    
    @WebFilter("/*")
    public class CharacterEncodingFilter implements Filter {
    	}
    
    }
    ```

    - web,xml
      - filter관련 부분 지워줌



## 21. 학습과제(사용자 입력을 통한 계산 요청)





## 참고

- 유튜브 채널 뉴렉처








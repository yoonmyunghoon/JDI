# 서블릿/JSP Study

## 33. 서버에서 페이지 전환해주기(redirect)

### 페이지 전환

- 현재 상태
  - 값을 입력하고 버튼을 누르면 서블릿으로 요청이감
  - 응답으로 흰색 백지페이지를 넘겨줌
  - 사용자가 다시 뒤로가기를 누르거나, calc.html을 주소창에 쳐서 페이지를 요청해서 돌아온 후, 다른 값을 입력해야 됨
  - 서버에서 바로 calc.html을 응답해주는 방법은 없나?

![57](servlet_JSP_images/57.png)

- redirect
  - 사용자의 요청에 대해 바로 서블릿이 응답을 해주는 것이 아니라, calc.html로 경로를 우회해버림

![58](servlet_JSP_images/58.png)

### 코드로 알아보자

- Calc2.java

```java
package com.reynold.web;

import java.io.IOException;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/calc2")
public class Calc2 extends HttpServlet {

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		ServletContext application = request.getServletContext();
		HttpSession session = request.getSession();
		Cookie[] cookies = request.getCookies();
		
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charser=UTF-8");
		
		String v_ = request.getParameter("v");
		String op = request.getParameter("operator");
		
		int v = 0;
		
		if(!v_.equals("")) {
			 v = Integer.parseInt(v_);
		}
		
		// 계산 
		if(op.equals("=")) {
			
			int x = 0;
			for(Cookie c : cookies) { 
				if(c.getName().equals("value")) {
					x = Integer.parseInt(c.getValue());
					break;
				}
			}
			
			
			int y = v;
			
			String operator = "";
			for(Cookie c : cookies) { 
				if(c.getName().equals("op")) {
					operator = c.getValue();
					break;
				}
			}
			
			
			int result = 0;
			
			if (operator.equals("+")) {
				result = x+y;
			} else {
				result = x-y; 
			}
			response.getWriter().printf("result is %d\n", result);
		// 값을 저장 
		} else {
			
			Cookie valueCookie = new Cookie("value", String.valueOf(v));
			Cookie opCookie = new Cookie("op", op);
			valueCookie.setPath("/calc2");
			valueCookie.setMaxAge(24*60*60);
			opCookie.setPath("/calc2");
			response.addCookie(valueCookie);
			response.addCookie(opCookie);
			
      // redirect를 통해 calc2.html을 바로 응답해줌, 바로 사용자가 저 페이지로 이동하게 해줌
			response.sendRedirect("/calc2.html");
		}
	}
}
```



## 34. 동적인 페이지(서버 페이지)의 필요성

### 좀 더 현실적인 계산기 프로그램

- 사용자가 값을 입력하고 버튼을 누르면 다시 계산기 페이지가 돌아오는데 이때, 이전에 입력했던 정보들이 함께 보여질 수 있도록 해야됨
- 단순한 정적인 html 문서가 아니라 동적으로 변하는 정보가 포함된 html 문서가 응답으로 와야함
- 즉, 사용자가 입력한 내용을 서버에서 페이지를 만들 때 끼워 넣어야 함

![59](servlet_JSP_images/59.png)

### 동적인 페이지(서버 페이지)의 필요성

- 쿠키를 읽어서 이 페이지에 심어줘야하는데 단순히 html문서를 redirect해주는 방법으로는 안될 것 같음

![60](servlet_JSP_images/60.png)

- 서블릿으로 이용해서 동적으로 만들어줘야할 것 같음
  - 서블릿으로 동적 페이지를 만든다는 것은 이미 존재했던 calc.html을 보내주는게 아니라
  - 요청이 오면 출력할 문서를 그때 바로 만들어서 보내줌, 이 때 출력할 값을 꽂아서 보내주는 것
  - 이런 문서, 요청이 있을 때, 그 때 만들어지는 문서를 동적인 문서라고 함
  - 동적인 페이지도 결과는 html이겠지만, 이미 존재했던 것이 아니라 요청에 따라서 그 때 만들어진 페이지임
  - 위치 상 서버쪽에서 만들어지는 것이다보니 서버 페이지라고도 함
  - 이 페이지는 html같은 정적인 파일이 아니라 서블릿으로 된 동적인 문서를 만드는 프로그램으로 대신해야됨

![61](servlet_JSP_images/61.png)

### 코드로 만들어보자

- calc3.html
  - 일단 정적 html문서를 만들어보자

```html
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
					<td class="output" colspan="4">0</td>
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

![62](servlet_JSP_images/62.png)

 

## 35. 처음이자 마지막으로 동적인 페이지 서블릿으로 직접 만들기

- 여기서 서블릿으로 동적인 페이지를 만들어보면서 문제점을 알아보고 JSP를 사용해야하는 이유를 알아보자

### 요청 Method에 따른 특화된 메소드들을 이용하기

![63](servlet_JSP_images/63.png)

- calc3.html
  - 정적 문서
  - 3+4이 그대로 나옴

```html
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
					<td class="output" colspan="4">3+4</td>
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

![64](servlet_JSP_images/64.png)

- CalcPage.java
  - html을 그대로 출력할 수 있도록해줌
  - 3+4를 계산한 값이 나옴
  - 동적인 표현이 가능함
  - 하지만, 너무 번거로움

```java
package com.reynold.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/calcpage")
public class CalcPage extends HttpServlet {

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charser=UTF-8");
		PrintWriter out = response.getWriter();
		
	
		
		out.write("<!DOCTYPE html>");
		out.write("<html>");
		out.write("<head>");
		out.write("<meta charset=\"UTF-8\">");
		out.write("<style>");
		out.write("input{");
		out.write("width:50px;");
		out.write("height:50px;");
		out.write("}");
		out.write(".output{");
		out.write("height:50px;");
		out.write("background: #e9e9e9;");
		out.write("font-size: 24px;");
		out.write("font-weight: bold;");
		out.write("text-align: right;");
		out.write("padding: 0px 5px;");
		out.write("}");
		out.write("</style>");
		out.write("<title>calculator</title>");
		out.write("</head>");
		out.write("<body>");
		out.write("<div>");
		out.write("<form action=\"calc3\" method=\"post\">");
		out.write("<table>");
		out.write("<tr>");
		out.printf("<td class=\"output\" colspan=\"4\">%d</td>", 3+4);
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"CE\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"C\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"BS\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"/\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"7\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"8\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"9\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"*\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"4\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"5\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"6\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"-\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"1\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"2\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"3\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"+\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"0\" /></td>");
		out.write("<td><input type=\"submit\" name=\"dot\" value=\".\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"=\" /></td>");
		out.write("</tr>");
		out.write("</table>");
		out.write("</form>");
		out.write("</div>");
		out.write("</body>");
		out.write("</html>");
	}
}
```

![65](servlet_JSP_images/65.png)



## 36. 계산기 서블릿 완성하기

- CalcPage.java

```java
package com.reynold.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/calcpage")
public class CalcPage extends HttpServlet {

	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		Cookie[] cookies = request.getCookies();

		String exp = "0";
		if (cookies != null) {
			for (Cookie c : cookies) {
				if (c.getName().equals("exp")) {
					exp = c.getValue();
					break;
				}
			}
		}

		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charser=UTF-8");
		PrintWriter out = response.getWriter();

		out.write("<!DOCTYPE html>");
		out.write("<html>");
		out.write("<head>");
		out.write("<meta charset=\"UTF-8\">");
		out.write("<style>");
		out.write("input{");
		out.write("width:50px;");
		out.write("height:50px;");
		out.write("}");
		out.write(".output{");
		out.write("height:50px;");
		out.write("background: #e9e9e9;");
		out.write("font-size: 24px;");
		out.write("font-weight: bold;");
		out.write("text-align: right;");
		out.write("padding: 0px 5px;");
		out.write("}");
		out.write("</style>");
		out.write("<title>calculator</title>");
		out.write("</head>");
		out.write("<body>");
		out.write("<div>");
		out.write("<form action=\"calc3\" method=\"post\">");
		out.write("<table>");
		out.write("<tr>");
		out.printf("<td class=\"output\" colspan=\"4\">%s</td>", exp);
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"CE\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"C\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"BS\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"/\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"7\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"8\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"9\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"*\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"4\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"5\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"6\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"-\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"1\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"2\" /></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"3\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"+\" /></td>");
		out.write("</tr>");
		out.write("<tr>");
		out.write("<td></td>");
		out.write("<td><input type=\"submit\" name=\"value\" value=\"0\" /></td>");
		out.write("<td><input type=\"submit\" name=\"dot\" value=\".\" /></td>");
		out.write("<td><input type=\"submit\" name=\"operator\" value=\"=\" /></td>");
		out.write("</tr>");
		out.write("</table>");
		out.write("</form>");
		out.write("</div>");
		out.write("</body>");
		out.write("</html>");

	}

}

```

- Calc3.java

```java
package com.reynold.web;

import java.io.IOException;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/calc3")
public class Calc3 extends HttpServlet {

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		Cookie[] cookies = request.getCookies();
		
		String value = request.getParameter("value");
		String operator = request.getParameter("operator");
		String dot = request.getParameter("dot");
		
		String exp = "";
		if (cookies != null) {
			for (Cookie c : cookies) {
				if (c.getName().equals("exp")) {
					exp = c.getValue();
					break;
				}
			}
		}
		
		if(operator != null && operator.equals("=")) {
			ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
			try {
				exp = String.valueOf(engine.eval(exp));
			} catch (ScriptException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		} else {
			exp += (value == null) ? "" : value;
			exp += (operator == null) ? "" : operator;
			exp += (dot == null) ? "" : dot;
		}

		
		Cookie expCookie = new Cookie("exp", exp);
		
		response.addCookie(expCookie);
		response.sendRedirect("calcpage");
		
	}

}

```





## 참고

- 유튜브 채널 뉴렉처








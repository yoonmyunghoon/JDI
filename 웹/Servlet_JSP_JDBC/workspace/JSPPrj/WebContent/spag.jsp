<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<%
pageContext.setAttribute("result", "hello");
%>
<body>
	<%=request.getAttribute("result") %>입니다.
	${result}입니다.<br>
	${names[0]}
	${names[1]}<br>
	${notice.id}
	${notice.title}<br>
	<br>
	request의 result ===> ${requestScope.result}<br>
	page의 result ===> ${result}
	<br>
	<br>
	${param.n}<br>
	${header.accept}<br>
	<br>
	${param.n <= 3}<br>
	${param.n gt 3}<br>
	${not empty param.n ? param.n : '값이 비어 있습니다.'}<br>
	${param.n/3}<br>
	
</body>
</html>
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
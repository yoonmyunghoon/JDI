# JSP 학습 2



## 53. 자세한 페이지 구현하기

### 목록 페이지와 자세한 페이지

![49](JSP_images/49.png)

- list.jsp
  - 파라미터로 id를 전달해주자

```jsp
<% while(rs.next()){ %>
							
					<tr>
						<td><%= rs.getInt("ID") %></td>
						<td class="title indent text-align-left"><a href="detail.jsp?id=<%= rs.getInt("ID") %>"><%= rs.getString("TITLE") %></a></td>
						<td><%= rs.getString("WRITER_ID") %></td>
						<td>
							<%= rs.getDate("REGDATE") %>		
						</td>
						<td><%= rs.getInt("HIT") %></td>
					</tr>
							
					<% }%>
```

- detail.jsp
  - select문으로 id에 해당하는 게시글을 가져옴
  - 결과를 적절한 위치에서 보여줄 수 있도록 해줌
  - 목록 버튼을 누르면 list.jsp로 가도록 링크 수정

```jsp
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%
	int id = Integer.parseInt(request.getParameter("id"));

	String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
	String sql = "SELECT * FROM NOTICE WHERE ID=?";
	
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con = DriverManager.getConnection(url, "NEWLEC", "1234");
	PreparedStatement st = con.prepareStatement(sql);
	st.setInt(1, id);
	ResultSet rs = st.executeQuery();
	rs.next();
%>

    <!-- header 부분 -->


            <!-- ---------------------------<header>--------------------------------------- -->


	<!-- --------------------------- <visual> --------------------------------------- -->
	<!-- visual 부분 -->
	

	<!-- --------------------------- <body> --------------------------------------- -->


			<!-- --------------------------- aside --------------------------------------- -->
			<!-- aside 부분 -->


			<!-- --------------------------- main --------------------------------------- -->

			


			<main>
				<h2 class="main title">공지사항</h2>
				
				<div class="breadcrumb">
					<h3 class="hidden">breadlet</h3>
					<ul>
						<li>home</li>
						<li>고객센터</li>
						<li>공지사항</li>
					</ul>
				</div>
				
				<div class="margin-top first">
						<h3 class="hidden">공지사항 내용</h3>
						<table class="table">
							<tbody>
								<tr>
									<th>제목</th>
									<td class="text-align-left text-indent text-strong text-orange" colspan="3"><%= rs.getString("TITLE") %></td>
								</tr>
								<tr>
									<th>작성일</th>
									<td class="text-align-left text-indent" colspan="3"><%= rs.getDate("REGDATE") %></td>
								</tr>
								<tr>
									<th>작성자</th>
									<td><%= rs.getString("WRITER_ID") %></td>
									<th>조회수</th>
									<td><%= rs.getString("HIT") %></td>
								</tr>
								<tr>
									<th>첨부파일</th>
									<td colspan="3"><%= rs.getString("FILES") %></td>
								</tr>
								<tr class="content">
									<td colspan="4"><%= rs.getString("CONTENT") %></td>
								</tr>
							</tbody>
						</table>
					</div>
					
					<div class="margin-top text-align-center">
						<a class="btn btn-list" href="list.jsp">목록</a>
					</div>
					
					<div class="margin-top">
						<table class="table border-top-default">
							<tbody>
								
								<tr>
									<th>다음글</th>
									<td colspan="3"  class="text-align-left text-indent">다음글이 없습니다.</td>
								</tr>
								
									
								
								
								<tr>
									<th>이전글</th>
									<td colspan="3"  class="text-align-left text-indent"><a class="text-blue text-strong" href="">스프링 DI 예제 코드</a></td>
								</tr>
								
								
							</tbody>
						</table>
					</div>			
					
			</main>		
			
		</div>
	</div>

    <!-- ------------------- <footer> --------------------------------------- -->

    <% 
    rs.close();
	st.close();
	con.close();
    %>
```



## 54. 자세한 페이지 MVC model1으로 변경하기

### 스파게티 코드로 작성된 noticeDetail.jsp 페이지

![50](JSP_images/50.png)

### 임시 변수를 이용한 코드 분리

![51](JSP_images/51.png)

- detail.jsp
  - Control부분(자바코드)을 위쪽으로, View부분(html코드)를 밑으로 몰아서 양분화시킴
  - 유지보수에 용이함

```jsp
<%@page import="java.util.Date"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%
	int id = Integer.parseInt(request.getParameter("id"));

	String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
	String sql = "SELECT * FROM NOTICE WHERE ID=?";
	
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con = DriverManager.getConnection(url, "NEWLEC", "1234");
	PreparedStatement st = con.prepareStatement(sql);
	st.setInt(1, id);
	ResultSet rs = st.executeQuery();
	rs.next();
	
	String title = rs.getString("TITLE");
	String writerId = rs.getString("WRITER_ID");
	Date regdate = rs.getDate("REGDATE");
	String hit = rs.getString("HIT");
	String files = rs.getString("FILES");
	String content = rs.getString("CONTENT");

    rs.close();
	st.close();
	con.close();
%>

<!DOCTYPE html>
<html>

<head>
    <title>코딩 전문가를 만들기 위한 온라인 강의 시스템</title>
    <meta charset="UTF-8">
    <title>공지사항목록</title>
    
    <link href="/css/customer/layout.css" type="text/css" rel="stylesheet" />
    <style>
    
        #visual .content-container{	
            height:inherit;
            display:flex; 
            align-items: center;
            
            background: url("../../images/customer/visual.png") no-repeat center;
        }
    </style>
</head>

<body>
    <!-- header 부분 -->

	<header id="header">
        
        <div class="content-container">
            <!-- ---------------------------<header>--------------------------------------- -->

            <h1 id="logo">
                <a href="/index.html">
                    <img src="/images/logo.png" alt="뉴렉처 온라인" />

                </a>
            </h1>

            <section>
                <h1 class="hidden">헤더</h1>

                <nav id="main-menu">
                    <h1>메인메뉴</h1>
                    <ul>
                        <li><a href="/guide">학습가이드</a></li>

                        <li><a href="/course">강좌선택</a></li>
                        <li><a href="/answeris/index">AnswerIs</a></li>
                    </ul>
                </nav>

                <div class="sub-menu">

                    <section id="search-form">
                        <h1>강좌검색 폼</h1>
                        <form action="/course">
                            <fieldset>
                                <legend>과정검색필드</legend>
                                <label>과정검색</label>
                                <input type="text" name="q" value="" />
                                <input type="submit" value="검색" />
                            </fieldset>
                        </form>
                    </section>

                    <nav id="acount-menu">
                        <h1 class="hidden">회원메뉴</h1>
                        <ul>
                            <li><a href="/index.html">HOME</a></li>
                            <li><a href="/member/login.html">로그인</a></li>
                            <li><a href="/member/agree.html">회원가입</a></li>
                        </ul>
                    </nav>

                    <nav id="member-menu" class="linear-layout">
                        <h1 class="hidden">고객메뉴</h1>
                        <ul class="linear-layout">
                            <li><a href="/member/home"><img src="/images/txt-mypage.png" alt="마이페이지" /></a></li>
                            <li><a href="/notice/list.html"><img src="/images/txt-customer.png" alt="고객센터" /></a></li>
                        </ul>
                    </nav>

                </div>
            </section>

        </div>
        
    </header>

	<!-- --------------------------- <visual> --------------------------------------- -->
	<!-- visual 부분 -->
	
	<div id="visual">
		<div class="content-container"></div>
	</div>
	<!-- --------------------------- <body> --------------------------------------- -->
	<div id="body">
		<div class="content-container clearfix">

			<!-- --------------------------- aside --------------------------------------- -->
			<!-- aside 부분 -->


			<aside class="aside">
				<h1>고객센터</h1>

				<nav class="menu text-menu first margin-top">
					<h1>고객센터메뉴</h1>
					<ul>
						<li><a class="current"  href="/customer/notice">공지사항</a></li>
						<li><a class=""  href="/customer/faq">자주하는 질문</a></li>
						<li><a class="" href="/customer/question">수강문의</a></li>
						<li><a class="" href="/customer/event">이벤트</a></li>
						
					</ul>
				</nav>


	<nav class="menu">
		<h1>협력업체</h1>
		<ul>
			<li><a target="_blank" href="http://www.notepubs.com"><img src="/images/notepubs.png" alt="노트펍스" /></a></li>
			<li><a target="_blank" href="http://www.namoolab.com"><img src="/images/namoolab.png" alt="나무랩연구소" /></a></li>
						
		</ul>
	</nav>
					
			</aside>
			<!-- --------------------------- main --------------------------------------- -->

			


			<main>
				<h2 class="main title">공지사항</h2>
				
				<div class="breadcrumb">
					<h3 class="hidden">breadlet</h3>
					<ul>
						<li>home</li>
						<li>고객센터</li>
						<li>공지사항</li>
					</ul>
				</div>
				
				<div class="margin-top first">
						<h3 class="hidden">공지사항 내용</h3>
						<table class="table">
							<tbody>
								<tr>
									<th>제목</th>
									<td class="text-align-left text-indent text-strong text-orange" colspan="3"><%=title %></td>
								</tr>
								<tr>
									<th>작성일</th>
									<td class="text-align-left text-indent" colspan="3"><%=regdate %></td>
								</tr>
								<tr>
									<th>작성자</th>
									<td><%=writerId %></td>
									<th>조회수</th>
									<td><%=hit %></td>
								</tr>
								<tr>
									<th>첨부파일</th>
									<td colspan="3"><%=files %></td>
								</tr>
								<tr class="content">
									<td colspan="4"><%=content %></td>
								</tr>
							</tbody>
						</table>
					</div>
					
					<div class="margin-top text-align-center">
						<a class="btn btn-list" href="list.jsp">목록</a>
					</div>
					
					<div class="margin-top">
						<table class="table border-top-default">
							<tbody>
								
								<tr>
									<th>다음글</th>
									<td colspan="3"  class="text-align-left text-indent">다음글이 없습니다.</td>
								</tr>
								
									
								
								
								<tr>
									<th>이전글</th>
									<td colspan="3"  class="text-align-left text-indent"><a class="text-blue text-strong" href="">스프링 DI 예제 코드</a></td>
								</tr>
								
								
							</tbody>
						</table>
					</div>			
					
			</main>		
			
		</div>
	</div>

    <!-- ------------------- <footer> --------------------------------------- -->



        <footer id="footer">
            <div class="content-container">
                <h2 id="footer-logo"><img src="/images/logo-footer.png" alt="회사정보"></h2>
    
                <div id="company-info">
                    <dl>
                        <dt>주소:</dt>
                        <dd>서울특별시 </dd>
                        <dt>관리자메일:</dt>
                        <dd>admin@newlecture.com</dd>
                    </dl>
                    <dl>
                        <dt>사업자 등록번호:</dt>
                        <dd>111-11-11111</dd>
                        <dt>통신 판매업:</dt>
                        <dd>신고제 1111 호</dd>
                    </dl>
                    <dl>
                        <dt>상호:</dt>
                        <dd>뉴렉처</dd>
                        <dt>대표:</dt>
                        <dd>홍길동</dd>
                        <dt>전화번호:</dt>
                        <dd>111-1111-1111</dd>
                    </dl>
                    <div id="copyright" class="margin-top">Copyright ⓒ newlecture.com 2012-2014 All Right Reserved.
                        Contact admin@newlecture.com for more information</div>
                </div>
            </div>
        </footer>
    </body>
    
    </html>
```



## 55. MVC model2 방식으로 변경하기





## 참고

- 유튜브 채널 뉴렉처








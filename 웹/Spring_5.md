# Spring Framework and Boot 학습 5 - Spring MVC

![1](Spring_images/1.png)



## 15. Tiles 지시서 작성하기

### MVC Model2와 Tiles

- 사용자가 요청을 함
  - /notice/list
- 디스패처서블릿이 컨트롤에게 요청을 전달
- 컨트롤은 요청에 해당하는 작업을 하고 결과로 모델과 뷰를 다시 디스패처서블릿에게 전달
  - 이때, 스프링이 제공하는 resolver를 사용해서 해당 위치에 있는 jsp를 찾아서 전달해줬음
    - 컨트롤러는 notice/list라는 값과 resolver를 통한 prefix와 subfix를 사용해서 jsp의 위치를 전달
  - 이제는 이런 형태말고도 notice.list 형태로 값을 반환해서 tiles를 호출하게 됨
    - tiles는 이런 형태의 값을 받으면 그 형태에 맞는 페이지 조각들을 조합해서 반환하게 됨
    - 어떤 페이지 조각들이 어떻게 결합되어야하는지 tiles가 알 수 있도록 지시서를 작성해줘야함
- 스프링은 어떻게 두 가지 형태(notice/list or notice.list)를 구분해서 처리해주는가?
  - tiles를 사용하는 형태의 우선순위를 높게 설정
  - tiles를 통해서 찾아보다가 없으면 resolver를 사용하는 방법
- tiles 지시사항에는 두가지가 있어야함
  -  어떤 조각을 붙일 것인지에 대한 지시사항
  - 어떤 위치에 붙여야되는지에 대한 지시사항

![89](Spring_images/89.png)

- Tiles
  - tiles는 백엔드에서 페이지를 처리할 때 사용되는 라이브러리
  - 페이지를 처리하는 부분이 백엔드에서 프론트엔드로 넘어가면서 tiles를 이용하는 빈도가 적어짐
  - 더 이상 발전하지는 않지만, 사용될 수도 있음
  - tutorial 링크
    - https://tiles.apache.org/framework/tutorial/basic/pages.html

![90](Spring_images/90.png)

- WEB-INF 안에 tiles.xml 생성

![91](Spring_images/91.png)

- ListController.java

```java
package com.newlecture.web.controller.notice;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class ListController implements Controller{

	@Override
	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
		
    // 변경해주기
		ModelAndView mv = new ModelAndView("notice.list");
//		ModelAndView mv = new ModelAndView("notice/list");
		return mv;
	}

}

```

- DetailController.java

```java
package com.newlecture.web.controller.notice;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class DetailController implements Controller{

	@Override
	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {

		ModelAndView mv = new ModelAndView("notice.detail");
		return mv;
	}

}

```

- tiles.xml
  - 레이아웃과 그 안에 들어갈 페이지 조각들을 작성해줬음
  - 각 조각들이 레이아웃의 어디에 위치할 것인지에 대한 설정 부분은 다음 챕터에서 알아보자

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tiles-definitions PUBLIC
       "-//Apache Software Foundation//DTD Tiles Configuration 3.0//EN"
       "http://tiles.apache.org/dtds/tiles-config_3_0.dtd">
<tiles-definitions>
  <definition name="notice.list" template="/WEB-INF/view/customer/inc/layout.jsp">
    <put-attribute name="title" value="Tiles tutorial homepage" />
    <put-attribute name="header" value="/WEB-INF/view/inc/header.jsp" />
    <put-attribute name="visual" value="/WEB-INF/view/customer/inc/visual.jsp" />
    <put-attribute name="aside" value="/WEB-INF/view/customer/inc/aside.jsp" />
    <put-attribute name="body" value="/WEB-INF/view/customer/notice/list.jsp" />
    <put-attribute name="footer" value="/WEB-INF/view/inc/footer.jsp" />
  </definition>
  <definition name="notice.detail" template="/WEB-INF/view/customer/inc/layout.jsp">
    <put-attribute name="title" value="Tiles tutorial homepage" />
    <put-attribute name="header" value="/WEB-INF/view/inc/header.jsp" />
    <put-attribute name="visual" value="/WEB-INF/view/customer/inc/visual.jsp" />
    <put-attribute name="aside" value="/WEB-INF/view/customer/inc/aside.jsp" />
    <put-attribute name="body" value="/WEB-INF/view/customer/notice/detail.jsp" />
    <put-attribute name="footer" value="/WEB-INF/view/inc/footer.jsp" />
  </definition>
</tiles-definitions>
```



## 16. 레이아웃 페이지 만들기와 Tiles 라이브러리 설정하기

- tiles.xml에서 레이아웃에 어떤 페이지 조각들을 넣을 것인지에 대한 설정을 해줬음
- 이제는 어떤 위치에 둘 것인지에 대한 설정을 해줘야함
- layout.jsp에서 taglib를 사용할 수 있도록 tiles 라이브러리를 받아오자
  - https://mvnrepository.com/artifact/org.apache.tiles/tiles-jsp/3.0.8
- pom.xml

```xml
<!-- https://mvnrepository.com/artifact/org.apache.tiles/tiles-jsp -->
<dependency>
  <groupId>org.apache.tiles</groupId>
  <artifactId>tiles-jsp</artifactId>
  <version>3.0.8</version>
</dependency>
```

- titles.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tiles-definitions PUBLIC
       "-//Apache Software Foundation//DTD Tiles Configuration 3.0//EN"
       "http://tiles.apache.org/dtds/tiles-config_3_0.dtd">
<tiles-definitions>
  <definition name="notice.list" template="/WEB-INF/view/customer/inc/layout.jsp">
    <put-attribute name="title" value="공지사항" />
    <put-attribute name="header" value="/WEB-INF/view/inc/header.jsp" />
    <put-attribute name="visual" value="/WEB-INF/view/customer/inc/visual.jsp" />
    <put-attribute name="aside" value="/WEB-INF/view/customer/inc/aside.jsp" />
    <put-attribute name="body" value="/WEB-INF/view/customer/notice/list.jsp" />
    <put-attribute name="footer" value="/WEB-INF/view/inc/footer.jsp" />
  </definition>
  <definition name="notice.detail" template="/WEB-INF/view/customer/inc/layout.jsp">
    <put-attribute name="title" value="Tiles tutorial homepage" />
    <put-attribute name="header" value="/WEB-INF/view/inc/header.jsp" />
    <put-attribute name="visual" value="/WEB-INF/view/customer/inc/visual.jsp" />
    <put-attribute name="aside" value="/WEB-INF/view/customer/inc/aside.jsp" />
    <put-attribute name="body" value="/WEB-INF/view/customer/notice/detail.jsp" />
    <put-attribute name="footer" value="/WEB-INF/view/inc/footer.jsp" />
  </definition>
</tiles-definitions>
```

- layout.jsp
  - taglib 추가
  - 각 위치에 맞는 페이지 조각을 tiles태그를 사용해서 넣어주자

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="tiles" uri="http://tiles.apache.org/tags-tiles" %>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title><tiles:getAsString name="title" /></title>
    
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
	<tiles:insertAttribute name="header" />

	<!-- --------------------------- <visual> --------------------------------------- -->
	<!-- visual 부분 -->
	<tiles:insertAttribute name="visual" />
	
	<!-- --------------------------- <body> --------------------------------------- -->
	<div id="body">
		<div class="content-container clearfix">

			<!-- --------------------------- aside --------------------------------------- -->
			<!-- aside 부분 -->
			<tiles:insertAttribute name="aside" />

			
			<!-- --------------------------- main --------------------------------------- -->
			<tiles:insertAttribute name="body" />
			
		</div>
	</div>

    <!-- ------------------- <footer> --------------------------------------- -->
	<tiles:insertAttribute name="footer" />

    </body>
    
    </html>
```



## 17. Tiles ViewResolver 설정하기









## 참고

- 유튜브 채널 - 뉴렉처
  - 스프링 프레임워크 강좌/강의
  - https://www.youtube.com/watch?v=XtXHIDnzS9c&list=PLq8wAnVUcTFUHYMzoV2RoFoY2HDTKru3T


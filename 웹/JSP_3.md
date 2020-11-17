# JSP 학습 3



## 62. forEach의 속성 사용하기

### JSTL Core

- 여기서 빨간색 박스 안에 있는 것들을 공부할 것
- 나머지는 예전에 사용되던 것들, 현재 방식에는 안맞기 때문에 사용하지 않는 것이 바람직함

![65](JSP_images/65.png)

### forEach

- 태그 속성에는 var, items, begin, end, varStatus, step 등이 있음
- varStatus는 반복문 한번 돌떄마다의 상태 정보를 가지고 있음
  - current: 반복하고 있는 객체
  - index: 반복하고 있는 객체의 인덱스
  - count: 반복횟수
  - first: 현재 반복되고 있는 객체가 첫번째이면 True, 아니면 False
  - last: 현재 반복되고 있는 객체가 마지막이면 True, 아니면 False
  - begin: begin 속성에서 넣어준 값을 보여줌
  - end: end 속성에서 넣어준 값을 보여줌
  - step: step 속성에서 넣어준 값을 보여줌

![66](JSP_images/66.png)



## 63. JSTL: forEach문으로 Pager 번호 만들기 - c:forEach

### pager 번호 생성하기

![67](JSP_images/67.png)

- list.jsp
  - c:set 태그를 통해 변수를 설정해줄 수 있고, 이 변수는 pageContext에 저장되어 페이지 내에서 사용될 수 있음 

```jsp
<c:set var="page" value="${(param.p == null)?1:param.p}"/>
<c:set var="startNum" value="${page-(page-1)%5}"/>
<ul class="-list- center">
  <c:forEach var="i" begin="0" end="4">
    <li><a class="-text- orange bold" href="?p=${startNum+i}&t=&q=" >${startNum+i}</a></li>
  </c:forEach>
</ul>
```



## 64. JSTL: if 문으로 Pager 이전/다음 번호 만들기 - c:if

- list.jsp
  - lastNum은 레코드의 총 개수와 연관이 있지만, 여기서는 JSTL을 중심으로 볼 것이기 때문에 임의로 23을 넣어줌
  - JSTL의 if 문의 경우, else문이 따로 없기 때문에 조건문 자체를 배타적으로 설정해줘야함
  - startNum을 기준으로해서 조건문을 처리해주자

```jsp
<c:set var="page" value="${(param.p == null)?1:param.p}"/>
<c:set var="startNum" value="${page-(page-1)%5}"/>
<c:set var="lastNum" value="23"/>

<div>	
  <c:if test="${startNum>1}">
    <a href="?p=${startNum-1}&t=&q=" class="btn btn-prev">이전</a>
  </c:if>
  <c:if test="${startNum<=1}">
    <span class="btn btn-prev" onclick="alert('이전 페이지가 없습니다.');">이전</span>
  </c:if>
</div>

<ul class="-list- center">
  <c:forEach var="i" begin="0" end="4">
    <li><a class="-text- orange bold" href="?p=${startNum+i}&t=&q=" >${startNum+i}</a></li>
  </c:forEach>
</ul>

<div>
  <c:if test="${startNum+5<lastNum}">
    <a href="?p=${startNum+5}&t=&q=" class="btn btn-next">다음</a>
  </c:if>
  <c:if test="${startNum+5>=lastNum}">
    <span class="btn btn-next" onclick="alert('다음 페이지가 없습니다.');">다음</span>
  </c:if>
</div>
```



## 65. JSTL: forTokens로 첨부파일 목록 출력하기 - c:forTockens

- detail.jsp
  - 첨부파일 목록을 구분자(,)로 구분해서 분리하고, 반복해서 출력해줌

```jsp
<tr>
  <th>첨부파일</th>
  <td colspan="3" style="text-align:Left;text-indent:10px;">
    <c:forTokens var="fileName" items="${n.files}" delims="," varStatus="st">
      <a href="${fileName}">${fileName}</a>
      <c:if test="${!st.last}">
        /
      </c:if>
    </c:forTokens>
  </td>
</tr>
```

- 결과

![68](JSP_images/68.png)



## 66. JSTL: format 태그로 날짜 형식 변경하기 - fmt:formatDate

- list.jsp
  - DB에 저장되어있는 date 값을 jsp가 알아서 변경해준 상태인데, 이것을 내가 원하는 형태로 만들 수 있음
  - fmt:formatDate태그를 사용해서 yyyy-MM-dd 형태로 표현

```jsp
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<c:forEach var="n" items="${list}">
  <tr>
    <td>${n.id}</td>
    <td class="title indent text-align-left"><a href="detail?id=${n.id}">${n.title}</a></td>
    <td>${n.writerId}</td>
    <td><fmt:formatDate pattern="yyyy-MM-dd" value="${n.regdate}"/></td>
    <td>${n.hit}</td>
  </tr>
</c:forEach>
```

- 결과

![69](JSP_images/69.png)

- detail.jsp
  - yyyy-MM-dd hh:mm:ss 형태로 표현

```jsp
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<tr>
  <th>작성일</th>
  <td class="text-align-left text-indent" colspan="3"><fmt:formatDate pattern="yyyy-MM-dd hh:mm:ss" value="${n.regdate}"/></td>
</tr>
```

- 결과

![70](JSP_images/70.png)



## 67. JSTL: format 태그로 숫자 출력 형식 지정하기 - fmt:formatNumber





## 참고

- 유튜브 채널 뉴렉처








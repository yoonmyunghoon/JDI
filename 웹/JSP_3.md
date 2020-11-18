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

- detail.jsp
  - 이렇게만해도 기본적으로 세자리씩 끊어줌
  - 이외에도 여러가지 속성값들이 존재하고 필요에 따라 찾아서 쓰면 됨

```jsp
<th>조회수</th>
<td><fmt:formatNumber value="${n.hit}" /></td>
```

- 결과

![71](JSP_images/71.png)



## 68. JSTL:functions로 EL에서 함수 이용하기

- 문자열을 조작할려고 할때 사용할 수 있음
- functions 태그는 EL표기법 안에 작성함
- detail.jsp
  - 첨부파일의 이름을 대문자로 표시하고, 만약 zip형식일 경우에는 빨간색 굻은 글자로 표현해보자

```jsp
<tr>
  <th>첨부파일</th>
  <td colspan="3" style="text-align:Left;text-indent:10px;">
    <c:forTokens var="fileName" items="${n.files}" delims="," varStatus="st">
      <c:set var="style" value="" />
      <c:if test="${fn:endsWith(fileName, '.zip')}">
        <c:set var="style" value="font-weight:bold; color:red;" />
      </c:if>
      <a href="${fileName}" style="${style}">${fn:toUpperCase(fileName)}</a>
      <c:if test="${!st.last}">
        /
      </c:if>
    </c:forTokens>
  </td>
</tr>
```

- 결과

![72](JSP_images/72.png)



## 69. 기업형으로 레이어를 나누는 이유와 설명 - 코드 분리를 위한 사전 설명

### 정리 - 코드의 분리

- 더 세밀하게 코드를 분리하는 이유
  - 실제 기업형 프로그램을 개발할 때는 규모가 크기 때문에 분업이 필요함

#### 서블릿만으로 이루어진 모델

- 요청에 대한 응답을 서블릿에서 모두 처리하는 형태

![73](JSP_images/73.png)

#### 서블릿과 jsp를 분리한 MVC 모델

- 지금까지 만든 형태가 이 형태임
- 문서 출력에 대한 부담을 줄이기 위해서 서블릿에서는 control역할을 담당하고 model을 정의해서 view(jsp)에게 전달함
- 사용자의 입력 및 출력 관리와 업무 처리를 control에서 함
- 혼자 개발하고 서비스할 때는 이런 방식이 적합함
  - 팀으로 개발을 할 때는 분업해야함
  - 좀 더 적합한 방식이 있음

![74](JSP_images/74.png)

#### 트랜잭션을 처리하는 업무 서비스를 분리함

- 경험이 많은 사람은 업무 서비스를, 그렇지 않은 사람은 입출력을 맡도록 분업하는 것이 바람직
  - 업무를 제대로 알고 구현하는 것이 중요하기 때문임
  - 입출력에서의 오류보다 업무관련된 데이터의 손실이나 오류가 더 큰 피해로 이어짐
- 실제 업무(비즈니스 로직)와 관련된 처리들은 업무 서비스에서 담당함
  - 예를 들어 결제 시스템이라면 결제와 관련된 기능들을 여기서 담당하는 것
  - 만약 계좌이체를 사용자가 요청하면 서블릿(control)이 여기로 바로 요청을 전달하고, 여기서 관련 기능들을 구현하고, 결과를 다시 서블릿(control)에게 전달함, 서블릿은 결과를 받아서 출력을 할 수 있도록 함
- 업무 서비스 부분은 잘 변경되지 않기 때문에 재사용에도 용이함

![75](JSP_images/75.png)

#### 데이터서비스(DAO)까지 분리한 경우

- 이전의 모델에서는 업무 서비스에서 DB와 관련된 처리를 함께 했다면, 이부분도 분리하는 것
- 어떤 DBMS를 사용하는지, 어떤 형식으로 데이터가 제공되는지 이런 부분들은 신경쓰지 않고, 업무 로직 처리에만 집중하기 위해서 분리하는 것
- 보통 기업형 프로그램을 개발할 때, 이런 형태로 분리해서 분업하는 것이 일반적임
- 계좌이체를 구현하고자 하면 두번의 update가 필요함(돈이 나가는 곳과 돈이 들어오는 곳의 데이터 갱신)
  - 이 과정에서 두번의 update 중 하나만 되는 일이 일어나지 않도록 업무 서비스에서 트랜잭션을 처리하는 부분도 관리해야함

![76](JSP_images/76.png)

#### 이외에도 다양한 형태가 가능함

- 상황에 맞게 선택할 수 있는 것
- 비즈니스 로직을 control에서 다 처리하고 싶으면 이런 형태도 가능함

![77](JSP_images/77.png)

- 또는 그냥 업무 서비스에서 데이터관련 처리도 함께 처리하겠다고 하면 이런 형태도 가능함
  - 일단은 이 방식부터 만들어보고, 이어서 DAO를 분리하는 식으로 진행하자
  - DAO를 분리하면서 발생하는 문제점과 이를 처리하기 위한 방법으로 스프링이 등장하게 됨

![78](JSP_images/78.png)



## 70. 서비스 함수 찾아내기

- Control에서 업무 서비스(비즈니스 로직 처리) 부분을 떼어내자

### 공지 시스템

- 공지에 대한 서비스 클래스를 만들자
- 관리자는 일반회원을 상속하고 있음
- 먼저 공지목록조회와 공지상세조회 기능을 구현하자

![79](JSP_images/79.png)

### 공지목록조회에서의 요청 사항

- 사용자가 공지 목록을 요청하는 방식, 세가지
  - 공지사항이라는 버튼을 눌러서 공지사항 페이지를 요청
    - getNoticeList()
  - 공지사항 페이지 내에 있는 페이저 버튼을 눌러서 그에 맞는 공지사항 페이지 요청
    - getNoticeList(int page)
  - 검색을 통한 페이지 요청
    - getNoticeList(String field, String query, int page)
- 공지 사항의 게시글 개수를 요청
  - getNoticeCount()
  - getNoticeCount(String field, String query)

![80](JSP_images/80.png)

### 공지상세조회에서의 요청 사항

- id를 넘겨받아서 해당 공지글을 요청
  - getNotice(id)
- 다음 글과 이전 글을 요청
  - getNextNotice(id)
  - getPrevNotice(id)

![81](JSP_images/81.png)



## 71. 서비스 클래스 구현하기





## 참고

- 유튜브 채널 뉴렉처








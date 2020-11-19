# JSP 학습 4



## 81. 자세한 페이지 수정하기

- NoticeDetailController.java
  - 디테일 페이지의 서비스 로직(id를 전달받아서 해당 게시글의 정보를 가져오는 로직)을 서비스 레이어에게 줌
  - 코드가 훨씬 간결해짐

```java
package com.reynold.web.controller;

import com.reynold.web.entity.Notice;
import com.reynold.web.service.NoticeService;


@WebServlet("/notice/detail")
public class NoticeDetailController extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		int id = Integer.parseInt(request.getParameter("id"));

		NoticeService service = new NoticeService();
		Notice notice = service.getNotice(id);
		request.setAttribute("n", notice);

		request
		.getRequestDispatcher("/WEB-INF/view/notice/detail.jsp")
		.forward(request, response);

	}
}

```

- NoticeService.java
  - 전달받은 id를 가지고 DB에 접근해서 해당 게시글의 정보를 얻음
  - notice라는 Entity에 속성들을 저장해서 객체로 만들고 리턴해줌 

```java
public Notice getNotice(int id) {
		
		Notice notice = null;
		
		String sql = "SELECT * FROM NOTICE WHERE ID=?";
		
		String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";

		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con = DriverManager.getConnection(url, "NEWLEC", "1234");
			PreparedStatement st = con.prepareStatement(sql);
			st.setInt(1, id);
			
			ResultSet rs = st.executeQuery();
			
			if(rs.next()){
				
				int nid = rs.getInt("ID");
				String title = rs.getString("TITLE");
				String writerId = rs.getString("WRITER_ID");
				Date regdate = rs.getDate("REGDATE");
				String hit = rs.getString("HIT");
				String files = rs.getString("FILES");
				String content = rs.getString("CONTENT");
				
				notice = new Notice(
						nid,
						title,
						writerId,
						regdate,
						hit,
						files,
						content
						);
			}
			
			rs.close();
			st.close();
			con.close();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return notice;
	}
```



## 82. 목록에 댓글 수를 표함하려면?

- list.jsp
  - 제목 뒷쪽에 댓글의 수를 넣어줄 예정임

```jsp
<c:forEach var="n" items="${list}">
  <tr>
    <td>${n.id}</td>
    <td class="title indent text-align-left"><a href="detail?id=${n.id}">${n.title}</a><span>[3]</span></td>
    <td>${n.writerId}</td>
    <td><fmt:formatDate pattern="yyyy-MM-dd" value="${n.regdate}"/></td>
    <td>${n.hit}</td>
  </tr>
</c:forEach>
```

- 결과
  - 이런식으로 표현되도록 하자

![87](JSP_images/87.png)



## 83. 목록에 댓글 수를 포함하기 위한 쿼리문제

- 공지목록과 각 글에 대한 댓글 개수를 함께 구하는 sql 쿼리문

```sql
SELECT N.ID, N.TITLE, N.WRITER_ID, N.REGDATE, N.HIT, N.FILES, COUNT(C.ID) CMT_COUNT
FROM NOTICE N LEFT JOIN "COMMENT" C ON N.ID = C.NOTICE_ID
GROUP BY N.ID, N.TITLE, N.WRITER_ID, N.REGDATE, N.HIT, N.FILES
ORDER BY N.REGDATE DESC;
```

- 결과

![88](JSP_images/88.png)



## 84. 목록의 댓글 수를 위한 View 생성하기

- 기존의 getNoticeList(String field, String query, int page)에서 사용되었던 sql문
  - 여기서 NOTICE가 적혀있는 부분에 앞서 구한 sql문이 들어가야함
  - 두 개의 쿼리문을 합하면 너무 복잡하고 길어지기 때문에 앞서 구한 sql문으로 View를 생성하고 사용하자

```sql
SELECT * 
FROM (SELECT ROWNUM NUM, N.* 
  FROM (SELECT * FROM NOTICE WHERE "+field+" LIKE ? ORDER BY REGDATE DESC) N
     ) 
WHERE NUM BETWEEN ? AND ?;
```

- JDBC에서 만들었던 NOTICE_VIEW가 있기 때문에 이번에 만드는 View이름은 NOTICE_VIEW2로 하겠음
- NOTICE_VIEW2 생성 sql
  - view를 생성할 때는 필터링이나 정렬과 같은 것들을 안하고 원본 테이블에 필요한 컬럼을 추가한 정도로 만드는 것이 좋음

```sql
CREATE VIEW NOTICE_VIEW2
AS
SELECT N.ID, N.TITLE, N.WRITER_ID, N.REGDATE, N.HIT, N.FILES, COUNT(C.ID) CMT_COUNT
FROM NOTICE N LEFT JOIN "COMMENT" C ON N.ID = C.NOTICE_ID
GROUP BY N.ID, N.TITLE, N.WRITER_ID, N.REGDATE, N.HIT, N.FILES;
```

- getNoticeList에서 사용하는 sql문 수정하기

```sql
SELECT * 
FROM (SELECT ROWNUM NUM, N.* 
  FROM (SELECT * FROM NOTICE_VIEW2 WHERE "+field+" LIKE ? ORDER BY REGDATE DESC) N
     ) 
WHERE NUM BETWEEN ? AND ?;
```

- NoticeService.java
  - Notice라는 entity를 그대로 사용하려면 cmtCount라는 속성을 추가해줘야하는데 그것보다는 Notice를 상속하는 NoticeView entity를 만들어주는 것이 바람직
  - content 속성은 DB에서 안받아왔으므로 뺴줌
    - GROUP BY할 때 용량이커서 처리하기 어려워서 빼줌
  - CMT_COUNT값을 cmtCount로 받고 NoticeView에 값들을 저장해서 객체화하고 리턴해줌
    - 관련된 부분들에서 기존에 Notice로 되어있던 객체타입을 NoticeView로 변경해주자

```java
package com.reynold.web.service;

import com.reynold.web.entity.Notice;
import com.reynold.web.entity.NoticeView;

public class NoticeService {
	public List<NoticeView> getNoticeList(){
		
		return getNoticeList("title", "", 1);
	}
	
	public List<NoticeView> getNoticeList(int page){
			
		return getNoticeList("title", "", page);
	}
	
	public List<NoticeView> getNoticeList(String field, String query, int page){
		
		List<NoticeView> list = new ArrayList<>();
		
		String sql = "SELECT * FROM (" + 
				"    SELECT ROWNUM NUM, N.*" + 
				"    FROM (SELECT * FROM NOTICE_VIEW2 WHERE "+field+" LIKE ? ORDER BY REGDATE DESC) N" + 
				") " + 
				"WHERE NUM BETWEEN ? AND ?";
		
		String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";

		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con = DriverManager.getConnection(url, "NEWLEC", "1234");
			PreparedStatement st = con.prepareStatement(sql);
			st.setString(1, "%"+query+"%");
			st.setInt(2, 1+(page-1)*10);
			st.setInt(3, page*10);
			
			ResultSet rs = st.executeQuery();
			
			while(rs.next()){
				
				int id = rs.getInt("ID");
				String title = rs.getString("TITLE");
				String writerId = rs.getString("WRITER_ID");
				Date regdate = rs.getDate("REGDATE");
				String hit = rs.getString("HIT");
				String files = rs.getString("FILES");
//				String content = rs.getString("CONTENT");
				int cmtCount = rs.getInt("CMT_COUNT");
				
				NoticeView notice = new NoticeView(
						id,
						title,
						writerId,
						regdate,
						hit,
						files,
//						content,
						cmtCount
						);
				list.add(notice);
				
			}
			
			rs.close();
			st.close();
			con.close();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return list;
	}
	
	public int getNoticeCount() {
		
		return getNoticeCount("title", "");
	}

}

```

- NoticeListController.java
  - NoticeView를 import하고, getNoticeList로부터 받은 NoticeView객체 리스트를 list에 저장

```java
package com.reynold.web.controller;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.reynold.web.entity.Notice;
import com.reynold.web.entity.NoticeView;
import com.reynold.web.service.NoticeService;

@WebServlet("/notice/list")
public class NoticeListController extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String field_ = request.getParameter("f");
		String query_ = request.getParameter("q");
		String page_ = request.getParameter("p");
		
		String field = "title";
		if(field_ != null && !field_.equals("")) {
			field = field_;
		}
		
		String query = "";
		if(query_ != null && !query_.equals("")) {
			query = query_;
		}
		
		int page = 1;
		if(page_ != null && !page_.equals("")) {
			page = Integer.parseInt(page_);
		}
		
		NoticeService service = new NoticeService();
		List<NoticeView> list = service.getNoticeList(field, query, page);
		int count = service.getNoticeCount(field, query);
		
		request.setAttribute("list", list);
		request.setAttribute("count", count);
		
		request
		.getRequestDispatcher("/WEB-INF/view/notice/list.jsp")
		.forward(request, response);
	}
}

```

- NoticeView.java
  - Notice를 상속하고, 추가적으로  cmtCount 속성값만 멤버변수로 생성
  - 생성자에서 content는 빈무자열로 처리해주자

```java
package com.reynold.web.entity;

import java.util.Date;

public class NoticeView extends Notice {
	
	private int cmtCount;
	
	public int getCmtCount() {
		return cmtCount;
	}

	public void setCmtCount(int cmtCount) {
		this.cmtCount = cmtCount;
	}

	public NoticeView() {
		
	}
	
	public NoticeView(int id, String title, String writerId, Date regdate, String hit, String files, int cmtCount) {
		super(id, title, writerId, regdate, hit, files, "");
		this.cmtCount = cmtCount;
	}
}

```

- list.jsp
  - 댓글의 개수를 cmtCount로 받아서 표시해줌

```jsp
<c:forEach var="n" items="${list}">
  <tr>
    <td>${n.id}</td>
    <td class="title indent text-align-left"><a href="detail?id=${n.id}">${n.title}</a><span> [${n.cmtCount}]</span></td>
    <td>${n.writerId}</td>
    <td><fmt:formatDate pattern="yyyy-MM-dd" value="${n.regdate}"/></td>
    <td>${n.hit}</td>
  </tr>
</c:forEach>
```

- 결과

![89](JSP_images/89.png)



## 85. Index 페이지 추가하기

- Index.jsp
  - Index.html 파일을 이용해서 만들고, 위에 지시자만 달아주자

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
  pageEncoding="UTF-8"%>

<!-- index.html 내용 그대로 옮기기 -->
```

- IndexController.java
  - index 관련된 요청과 응답을 처리할 control 생성

```java
package com.reynold.web.controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/index")
public class IndexController extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		request
		.getRequestDispatcher("/WEB-INF/view/index.jsp")
		.forward(request, response);
	}
}

```

- controller 파일 구조 변경
  - notice 관련 controller들을 묶어주기

![90](JSP_images/90.png)

- index 페이지 결과

![91](JSP_images/91.png)



## 86. Admin 페이지를 위한 서비스 목록 추가하기

- 관리자홈의 공지사항 목록 페이지
  - 일괄공개 요청
    - pubNoticeAll(ids)
  - 일괄삭제 요청
    - removeNoticeAll(ids)
  - 글쓰기 페이지 요청

![92](JSP_images/92.png)

- 글쓰기 페이지
  - 공지등록 요청
    - insertNotice(notice)

![93](JSP_images/93.png)

- 관리자홈의 디테일페이지
  - 공지삭제 요청
    - deleteNotice(id)
  - 글수정 페이지 요청

![94](JSP_images/94.png)

- 글수정 페이지
  - 공지수정 요청
    - updateNotice(notice)

![95](JSP_images/95.png)

- index 페이지의 공지사항 파트
  - getNoticeNewestList()

![96](JSP_images/96.png)

- NoticeService.java
  - 앞서 말한 서비스 로직들을 추가해주기
  - 일단 형태만 갖춰두자

```java
package com.reynold.web.service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import com.reynold.web.entity.Notice;
import com.reynold.web.entity.NoticeView;

public class NoticeService {
	
	public int removeNoticeAll(int[] ids) {
		
		return 0;
	}
	
	public int pubNoticeAll(int[] ids) {
		
		return 0;
	}
	
	public int insertNotice(Notice notice){
		
		return 0;
	}
	
	public int deleteNotice(int id){
		
		return 0;
	}
	
	public int updateNotice(Notice notice){
		
		return 0;
	}
	
	public List<Notice> getNoticeNewestList(){
		
		return null;
	}
	
  // 밑에는 생략
}

```



## 87. Admin/index 페이지 만들기







## 참고

- 유튜브 채널 뉴렉처








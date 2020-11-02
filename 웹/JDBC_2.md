# JDBC 학습 2



## 13. CRUD를 담당하는 서비스 틀래스(NoticeService) 생성하기

### Notice 개체(클래스) 만들기 and SELECT 기능부 만들기

- Notice.java

```java
package com.newlecture.app.entity;

import java.util.Date;

public class Notice {
	private int id;
	private String title;
	private String writerId;
	private Date regDate;
	private String content;
	private int hit;
	
	public Notice() {
		
	}
	
	public Notice(int id, String title, String writerId, Date regDate, String content, int hit) {
		this.id = id;
		this.title = title;
		this.writerId = writerId;
		this.regDate = regDate;
		this.content = content;
		this.hit = hit;
	}


	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getWriterId() {
		return writerId;
	}
	public void setWriterId(String writerId) {
		this.writerId = writerId;
	}
	public Date getRegDate() {
		return regDate;
	}
	public void setRegDate(Date regDate) {
		this.regDate = regDate;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public int getHit() {
		return hit;
	}
	public void setHit(int hit) {
		this.hit = hit;
	}
	
	
}

```

- NoticeService.java

```java
package com.newlecture.app.service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import com.newlecture.app.entity.Notice;

public class NoticeService {
	public List<Notice> getList() throws ClassNotFoundException, SQLException{
		String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
		String sql = "SELECT * FROM NOTICE";
		
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con = DriverManager.getConnection(url, "NEWLEC", "1234");
		Statement st = con.createStatement();
		ResultSet rs = st.executeQuery(sql);
		
		List<Notice> list = new ArrayList<Notice>();
		
		while (rs.next()) {
			int id = rs.getInt("ID");
			String title = rs.getString("TITLE");
			String writerId = rs.getString("WRITER_ID");
			Date regDate = rs.getDate("REGDATE");
			String content = rs.getString("CONTENT");
			int hit = rs.getInt("hit");
			
			Notice notice = new Notice(
					id, title, writerId, regDate, content, hit
				);
			list.add(notice);
		}
		
		
		rs.close();
		st.close();
		con.close();
		
		return list;
	}
}

```



## 14. NoticeService 구현 마무리

- Notice.java

```java
package com.newlecture.app.entity;

import java.util.Date;

public class Notice {
	private int id;
	private String title;
	private String writerId;
	private Date regDate;
	private String content;
	private int hit;
	private String files;
	
	public Notice() {
		
	}
	
	public Notice(int id, String title, String writerId, Date regDate, String content, int hit, String files) {
		
		this.id = id;
		this.title = title;
		this.writerId = writerId;
		this.regDate = regDate;
		this.content = content;
		this.hit = hit;
		this.files = files;
	}


	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getWriterId() {
		return writerId;
	}
	public void setWriterId(String writerId) {
		this.writerId = writerId;
	}
	public Date getRegDate() {
		return regDate;
	}
	public void setRegDate(Date regDate) {
		this.regDate = regDate;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public int getHit() {
		return hit;
	}
	public void setHit(int hit) {
		this.hit = hit;
	}

	public String getFiles() {
		return files;
	}

	public void setFiles(String files) {
		this.files = files;
	}
	
	
}

```

- NoticeService.java

```java
package com.newlecture.app.service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import com.newlecture.app.entity.Notice;

public class NoticeService {
	private String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
	private String uid = "NEWLEC";
	private String pwd = "1234";
	private String driver = "oracle.jdbc.driver.OracleDriver";
	
	public List<Notice> getList() throws ClassNotFoundException, SQLException{
		String sql = "SELECT * FROM NOTICE";
		
		Class.forName(driver);
		Connection con = DriverManager.getConnection(url, uid, pwd);
		Statement st = con.createStatement();
		ResultSet rs = st.executeQuery(sql);
		
		List<Notice> list = new ArrayList<Notice>();
		
		while (rs.next()) {
			int id = rs.getInt("ID");
			String title = rs.getString("TITLE");
			String writerId = rs.getString("WRITER_ID");
			Date regDate = rs.getDate("REGDATE");
			String content = rs.getString("CONTENT");
			int hit = rs.getInt("hit");
			String files = rs.getString("FILES");
			
			Notice notice = new Notice(
					id, title, writerId, regDate, content, hit, files
				);
			list.add(notice);
		}
		
		
		rs.close();
		st.close();
		con.close();
		
		return list;
	}
	
	public int insert(Notice notice) throws ClassNotFoundException, SQLException {
		String title = notice.getTitle();
		String writerId = notice.getWriterId();
		String content = notice.getContent();
		String files = notice.getFiles();
		
		String sql = "INSERT INTO notice (" + 
				"    title," + 
				"    writer_id," + 
				"    content," + 
				"    files" + 
				") VALUES (?,?,?,?)";
		
		Class.forName(driver);
		Connection con = DriverManager.getConnection(url, uid, pwd);
		PreparedStatement st = con.prepareStatement(sql);
		st.setString(1, title);
		st.setString(2, writerId);
		st.setString(3, content);
		st.setString(4, files);
		int result = st.executeUpdate();
		
		st.close();
		con.close();
		
		return result;
	}
	
	public int update(Notice notice) throws ClassNotFoundException, SQLException {
		String title = notice.getTitle();
		String content = notice.getContent();
		String files = notice.getFiles();
		int id = notice.getId();
		
		String sql = "UPDATE NOTICE SET" + 
				"    TITLE=?," + 
				"    CONTENT=?," + 
				"    FILES=?" + 
				"WHERE ID=?";
		
		Class.forName(driver);
		Connection con = DriverManager.getConnection(url, uid, pwd);
		PreparedStatement st = con.prepareStatement(sql);
		st.setString(1, title);
		st.setString(2, content);
		st.setString(3, files);
		st.setInt(4, id);
		int result = st.executeUpdate();
		
		st.close();
		con.close();
		
		return result;
	}
	
	public int delete(int id) throws ClassNotFoundException, SQLException {		
		String sql = "DELETE NOTICE WHERE ID=?";
		
		Class.forName(driver);
		Connection con = DriverManager.getConnection(url, uid, pwd);
		PreparedStatement st = con.prepareStatement(sql);
		st.setInt(1, id);
		int result = st.executeUpdate();
		
		st.close();
		con.close();
		return result;
	}

}

```



## 15. 사용자 인터페이스 붙이기(공지사항 목록)

### 사용자 인터페이스

- 웹 기반
- 콘솔 기반
- 윈도우
- ...
- 등
- 여러가지 인터페이스를 사용할 수 있지만, 여기서는 콘솔기반으로 해보자
- 웹 기반은 JSP에서 다룸

### 목록에서 쿼리해야 할 내용

![36](JDBC_images/36.png)

- Program5.java

```java
package ex1;

import java.sql.SQLException;

import com.newlecture.app.console.NoticeConsole;

public class Program5 {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		NoticeConsole console = new NoticeConsole();
		console.printNoticeList();
		int menu = console.inputNoticeMenu();
		
		switch(menu) {
		case 1: // 상세조회 
			break;
		case 2: // 이전 
			break;
		case 3: // 다음 
			break;
		case 4: // 글쓰기
			break;
		}
	}

}

```

- NoticeConsole.java

```java
package com.newlecture.app.console;

import java.sql.SQLException;
import java.util.List;

import com.newlecture.app.entity.Notice;
import com.newlecture.app.service.NoticeService;

public class NoticeConsole {
	
	private NoticeService service;
	
	public NoticeConsole() {
		service = new NoticeService();
	}

	public void printNoticeList() throws ClassNotFoundException, SQLException {
		List<Notice> list = service.getList();
		
		System.out.println("--------------------------------------");
		System.out.printf("<공지사항> 총 %d 게시글\n", 12);
		System.out.println("--------------------------------------");
		for(Notice n : list) {
			System.out.printf("%d. %s / %s / %s\n", 
					n.getId(), 
					n.getTitle(), 
					n.getWriterId(), 
					n.getRegDate());
		}
		System.out.println("--------------------------------------");
		System.out.printf(" %d/%d pages\n", 1, 2);

	}

	public int inputNoticeMenu() {
		
		return 0;
	}

}

```

- 결과

![37](JDBC_images/37.png)







## 참고

- 유튜브 뉴렉처 채널
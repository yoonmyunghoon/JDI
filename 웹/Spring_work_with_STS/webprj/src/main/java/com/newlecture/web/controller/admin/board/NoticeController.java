package com.newlecture.web.controller.admin.board;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller("adminNoticeController")
@RequestMapping("/admin/board/notice/")
public class NoticeController {

	@RequestMapping("list")
	public String list() {
		
		return "";
	}

	@RequestMapping("reg")
	@ResponseBody
	public String reg(String title, String content, String category, String[] foods, String food) {
		for(String f : foods) {
			System.out.printf("I like food%s", f);
			System.out.println();
		}
		System.out.printf("My favorite food is food%s", food);
		return String.format("title:%s<br>content:%s<br>category:%s<br>", title, content, category);
	}
	
	@RequestMapping("edit")
	public String edit() {
		
		return "";
	}
	
	@RequestMapping("del")
	public String del() {
		
		return "";
	}
	
}

package com.reynold.web.controller;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

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
		
		// redirect: 다른 페이지로 요청을 전달하는 것
		// forward: 작업했던 내용들을 이전하는 것
		request
		.getRequestDispatcher("/WEB-INF/view/notice/detail.jsp")
		.forward(request, response);
		
		
		
	}
}

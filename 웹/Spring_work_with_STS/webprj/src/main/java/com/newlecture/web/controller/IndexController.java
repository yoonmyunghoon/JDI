package com.newlecture.web.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class IndexController {
	
	@RequestMapping("/index")
	public void aaaa() {
		System.out.println("sdafsf");
	}

//	@Override
//	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
//		
////		ModelAndView mv = new ModelAndView("/WEB-INF/view/index.jsp");
////		ModelAndView mv = new ModelAndView("index");
//		ModelAndView mv = new ModelAndView("root.index");
//		mv.addObject("data", "Hello Spring MVC");
////		mv.setViewName("/WEB-INF/view/index.jsp");
//		return mv;
//	}
	
	
}

package com.assistant.windfall.controller;

import com.assistant.windfall.dao.CourseDao;
import com.assistant.windfall.service.CourseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/course")
public class CourseController {
    @Autowired
    CourseService courseService;

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public String create(@RequestBody CourseDao courseDao) {
        courseService.insertCourse(courseDao);
        return "success";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public CourseDao search(@RequestParam(name = "id") Integer id) {
        return courseService.obtainCourseById(id);
    }
}

package com.assistant.windfall.controller;

import com.assistant.windfall.dao.TeacherDao;
import com.assistant.windfall.service.TeacherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/teacher")
public class TeacherController {
    @Autowired
    TeacherService teacherService;

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public String create(@RequestBody TeacherDao teacherDao) {
        teacherService.insertTeacher(teacherDao);
        return "success";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public TeacherDao search(@RequestParam(name = "id") Integer id) {
        return teacherService.obtainTeacherById(id);
    }

    @RequestMapping(value = "/list/", method = RequestMethod.GET)
    @ResponseBody
    public List<TeacherDao> list(@RequestParam(name = "pageNum") Integer pageNum, @RequestParam(name = "pageSize") Integer pageSize) {
        return teacherService.listTeacher(pageNum, pageSize);
    }
}

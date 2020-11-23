package com.assistant.windfall.service;

import com.assistant.windfall.dao.CourseDao;
import com.assistant.windfall.mbg.mapper.CourseMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Service
public class CourseService {
    @Autowired
    CourseMapper courseMapper;

    public CourseDao obtainCourseById(Integer id){
        return courseMapper.obtainCourseById(id);
    }

    public void insertCourse(CourseDao CourseDao){
        courseMapper.insertCourse(CourseDao);
    }

    @RequestMapping(value = "/list/", method = RequestMethod.GET)
    @ResponseBody
    public List<CourseDao> listCourse(int pageNum, int pageSize) {
        PageHelper.startPage(pageNum, pageSize);
        return courseMapper.listCourse();
    }
}

package com.assistant.windfall.service;

import com.assistant.windfall.dao.CourseDao;
import com.assistant.windfall.mbg.mapper.CourseMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

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
}

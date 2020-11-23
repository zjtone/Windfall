package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.CourseDao;

import java.util.List;

public interface CourseMapper {
    CourseDao obtainCourseById(Integer id);

    void insertCourse(CourseDao userDao);

    List<CourseDao> listCourse();
}

package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.CourseDao;

public interface CourseMapper {
    CourseDao obtainCourseById(Integer id);

    void insertCourse(CourseDao userDao);
}

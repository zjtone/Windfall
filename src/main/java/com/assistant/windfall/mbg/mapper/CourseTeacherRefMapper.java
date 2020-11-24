package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.CourseTeacherRefDao;

import java.util.List;

public interface CourseTeacherRefMapper {
    CourseTeacherRefDao obtainCourseTeacherRefById(Integer id);

    void insertCourseTeacherRef(CourseTeacherRefDao userDao);

    List<CourseTeacherRefDao> listCourseTeacherRef(Integer orgId);
}

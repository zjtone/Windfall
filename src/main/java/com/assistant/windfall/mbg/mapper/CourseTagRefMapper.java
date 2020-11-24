package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.CourseTagRefDao;

import java.util.List;

public interface CourseTagRefMapper {
    CourseTagRefDao obtainCourseTagRefById(Integer id);

    void insertCourseTagRef(CourseTagRefDao userDao);

    List<CourseTagRefDao> listCourseTagRef(Integer orgId);
}

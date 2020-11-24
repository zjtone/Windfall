package com.assistant.windfall.service;

import com.assistant.windfall.dao.CourseTeacherRefDao;
import com.assistant.windfall.mbg.mapper.CourseTeacherRefMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CourseTeacherRefService {
    @Autowired
    CourseTeacherRefMapper courseTeacherRefMapper;

    public CourseTeacherRefDao obtainCourseTeacherRefById(Integer id){
        return courseTeacherRefMapper.obtainCourseTeacherRefById(id);
    }

    public void insertCourseTeacherRef(CourseTeacherRefDao courseTeacherRefDao){
        courseTeacherRefMapper.insertCourseTeacherRef(courseTeacherRefDao);
    }

    public List<CourseTeacherRefDao> listCourseTeacherRef(int pageNum, int pageSize, Integer orgId) {
        PageHelper.startPage(pageNum, pageSize);
        return courseTeacherRefMapper.listCourseTeacherRef(orgId);
    }
}

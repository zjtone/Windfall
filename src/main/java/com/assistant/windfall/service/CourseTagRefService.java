package com.assistant.windfall.service;

import com.assistant.windfall.dao.CourseTagRefDao;
import com.assistant.windfall.mbg.mapper.CourseTagRefMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CourseTagRefService {
    @Autowired
    CourseTagRefMapper courseTagRefMapper;

    public CourseTagRefDao obtainCourseTagRefById(Integer id){
        return courseTagRefMapper.obtainCourseTagRefById(id);
    }

    public void insertCourseTagRef(CourseTagRefDao CourseTagRefDao){
        courseTagRefMapper.insertCourseTagRef(CourseTagRefDao);
    }

    public List<CourseTagRefDao> listCourseTagRef(int pageNum, int pageSize, Integer orgId) {
        PageHelper.startPage(pageNum, pageSize);
        return courseTagRefMapper.listCourseTagRef(orgId);
    }
}

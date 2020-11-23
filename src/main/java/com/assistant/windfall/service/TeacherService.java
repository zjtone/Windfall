package com.assistant.windfall.service;

import com.assistant.windfall.dao.TeacherDao;
import com.assistant.windfall.mbg.mapper.TeacherMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TeacherService {
    @Autowired
    TeacherMapper teacherMapper;

    public TeacherDao obtainTeacherById(Integer id){
        return teacherMapper.obtainTeacherById(id);
    }

    public void insertTeacher(TeacherDao TeacherDao){
        teacherMapper.insertTeacher(TeacherDao);
    }

    public List<TeacherDao> listTeacher(int pageNum, int pageSize){
        PageHelper.startPage(pageNum, pageSize);
        return teacherMapper.listTeacher();
    }
}

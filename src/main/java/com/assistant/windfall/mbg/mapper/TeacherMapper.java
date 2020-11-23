package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.TeacherDao;

import java.util.List;

public interface TeacherMapper {

    TeacherDao obtainTeacherById(Integer id);

    void insertTeacher(TeacherDao employeeDao);

    List<TeacherDao> listTeacher();
}

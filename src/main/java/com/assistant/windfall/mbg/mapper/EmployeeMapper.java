package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.EmployeeDao;

import java.util.List;

public interface EmployeeMapper {

    EmployeeDao obtainEmployeeById(Integer id);

    void insertEmployee(EmployeeDao employeeDao);

    List<EmployeeDao> listEmployee(Integer orgId);
}

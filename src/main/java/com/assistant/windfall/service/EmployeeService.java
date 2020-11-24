package com.assistant.windfall.service;

import com.assistant.windfall.dao.EmployeeDao;
import com.assistant.windfall.mbg.mapper.EmployeeMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EmployeeService {
    @Autowired
    EmployeeMapper employeeMapper;

    public EmployeeDao obtainEmployeeById(Integer id){
        return employeeMapper.obtainEmployeeById(id);
    }

    public void insertEmployee(EmployeeDao EmployeeDao){
        employeeMapper.insertEmployee(EmployeeDao);
    }

    public List<EmployeeDao> listEmployee(int pageNum, int pageSize, Integer orgId){
        PageHelper.startPage(pageNum, pageSize);
        return employeeMapper.listEmployee(orgId);
    }
}

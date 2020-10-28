package com.assistant.windfall.controller;

import com.assistant.windfall.dao.EmployeeDao;
import com.assistant.windfall.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/employee")
public class EmployeeController {
    @Autowired
    EmployeeService employeeService;

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public String create(@RequestBody EmployeeDao employeeDao) {
        employeeService.insertEmployee(employeeDao);
        return "success";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public EmployeeDao search(@RequestParam(name = "id") Integer id) {
        return employeeService.obtainEmployeeById(id);
    }

    @RequestMapping(value = "/list/", method = RequestMethod.GET)
    @ResponseBody
    public List<EmployeeDao> list(@RequestParam(name = "pageNum") Integer pageNum, @RequestParam(name = "pageSize") Integer pageSize) {
        return employeeService.listEmployee(pageNum, pageSize);
    }
}

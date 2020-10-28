package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class EmployeeDao {
    private Integer id;
    private String username;
    private String password;
    private Integer type = EmployeeType.EMPLOYEE;
    private String idCard;
    private String phone;
    private String email;
    private String openid;
    private Integer orgId;

    public static class EmployeeType{
        public static final Integer EMPLOYEE = 1, TEACHER = 2;
    }
}

package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserDao {
    private Integer id;
    private String username;
    private String password;
    private Integer type = UserType.CHILD;
    private String idCard;
    private String phone;
    private String email;
    private String openid;
    private Integer orgId;

    public static class UserType{
        public static final Integer PARENT = 0, CHILD = 1, MANAGER = 2, ADMIN = 3;
    }
}

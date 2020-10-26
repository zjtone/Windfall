package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.UserDao;

import java.util.List;

public interface UserMapper {

    UserDao obtainUserById(Integer id);

    void insertUser(UserDao userDao);

    List<UserDao> listUser();
}

package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.UserDao;

public interface UserMapper {

    UserDao obtainUserById(Integer id);

    void insertUser(UserDao userDao);
}

package com.assistant.windfall.service;

import com.assistant.windfall.dao.UserDao;
import com.assistant.windfall.mbg.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    UserMapper userMapper;

    public UserDao obtainUser(Integer id){
        return userMapper.selectUser(id);
    }
}

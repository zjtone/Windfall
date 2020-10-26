package com.assistant.windfall.service;

import com.assistant.windfall.dao.UserDao;
import com.assistant.windfall.mbg.mapper.UserMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {
    @Autowired
    UserMapper userMapper;

    public UserDao obtainUserById(Integer id){
        return userMapper.obtainUserById(id);
    }

    public void insertUser(UserDao userDao){
        userMapper.insertUser(userDao);
    }

    public List<UserDao> listUser(int pageNum, int pageSize){
        PageHelper.startPage(pageNum, pageSize);
        return userMapper.listUser();
    }
}

package com.assistant.windfall.controller;

import com.assistant.windfall.dao.UserDao;
import com.assistant.windfall.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/user")
public class UserController {
    @Autowired
    UserService userService;

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public String create(@RequestBody UserDao userDao) {
        userService.insertUser(userDao);
        return "success";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public UserDao search(@RequestParam(name = "id") Integer id) {
        return userService.obtainUserById(id);
    }

    @RequestMapping(value = "/list/", method = RequestMethod.GET)
    @ResponseBody
    public List<UserDao> list(@RequestParam(name = "pageNum") Integer pageNum, @RequestParam(name = "pageSize") Integer pageSize) {
        return userService.listUser(pageNum, pageSize);
    }
}

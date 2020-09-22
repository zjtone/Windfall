package com.assistant.windfall.controller;

import com.assistant.windfall.dao.UserDao;
import com.assistant.windfall.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/user")
public class UserController {
    @Autowired
    UserService userService;

    public String hello() {
        return "hello";
    }

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public String create(@RequestBody UserDao userDao) {
        return "a";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public UserDao search(@RequestParam(name = "id") Integer id) {
        return userService.obtainUser(id);
    }
}

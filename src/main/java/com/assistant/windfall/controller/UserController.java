package com.assistant.windfall.controller;

import com.assistant.windfall.dao.UserDao;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/user")
public class UserController {

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
    public String search(@RequestParam(name = "id") Long id) {
        return "" + id;
    }
}

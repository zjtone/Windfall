package com.assistant.windfall.controller;

import com.assistant.windfall.dao.OrgDao;
import com.assistant.windfall.dao.UserDao;
import com.assistant.windfall.service.OrgService;
import com.assistant.windfall.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/organization")
public class OrgController {
    @Autowired
    OrgService orgService;

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public String create(@RequestBody OrgDao orgDao) {
        orgService.insertOrg(orgDao);
        return "success";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public OrgDao search(@RequestParam(name = "id") Integer id) {
        return orgService.obtainOrgById(id);
    }
}

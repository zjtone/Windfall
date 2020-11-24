package com.assistant.windfall.controller;

import com.assistant.windfall.dao.TagDao;
import com.assistant.windfall.service.TagService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/tag")
public class TagController {
    @Autowired
    TagService tagService;

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public String create(@RequestBody TagDao tagDao) {
        tagService.insertTag(tagDao);
        return "" + tagDao.getId();
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public TagDao search(@RequestParam(name = "id") Integer id) {
        return tagService.obtainTagById(id);
    }

    @RequestMapping(value = "/list/", method = RequestMethod.GET)
    @ResponseBody
    public List<TagDao> list(@RequestParam(name = "pageNum", defaultValue = "0") Integer pageNum,
                             @RequestParam(name = "pageSize", defaultValue = "10") Integer pageSize,
                             @RequestParam(name = "orgId") Integer orgId) {
        return tagService.listTag(pageNum, pageSize, orgId);
    }
}

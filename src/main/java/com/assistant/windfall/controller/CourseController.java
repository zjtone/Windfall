package com.assistant.windfall.controller;

import com.assistant.windfall.dao.CourseDao;
import com.assistant.windfall.dao.CourseTagRefDao;
import com.assistant.windfall.dao.CourseTeacherRefDao;
import com.assistant.windfall.service.CourseService;
import com.assistant.windfall.service.CourseTagRefService;
import com.assistant.windfall.service.CourseTeacherRefService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
@RequestMapping("/course")
public class CourseController {
    @Autowired
    CourseService courseService;
    @Autowired
    CourseTagRefService courseTagRefService;
    @Autowired
    CourseTeacherRefService courseTeacherRefService;

    private Map<String, InsertRefsHandler> insertRefsHandlerMap;

    public CourseController() {
        System.out.println("init course controller");
        insertRefsHandlerMap = new HashMap<>();
        insertRefsHandlerMap.put("tags", (orgId, id, refs) -> {
            System.out.println("insert tags");
            for (Integer refId : refs) {
                CourseTagRefDao courseTagRefDao = new CourseTagRefDao(id, refId, orgId);
                courseTagRefService.insertCourseTagRef(courseTagRefDao);
            }
        });
        insertRefsHandlerMap.put("teachers", (orgId, id, refs) -> {
            System.out.println("insert teachers");
            for (Integer refId : refs) {
                CourseTeacherRefDao courseTeacherRefDao = new CourseTeacherRefDao(id, refId, orgId);
                courseTeacherRefService.insertCourseTeacherRef(courseTeacherRefDao);
            }
        });
    }

    @RequestMapping(value = "/", method = RequestMethod.POST)
    @ResponseBody
    public Integer create(@RequestBody CourseDao courseDao) {
        courseService.insertCourse(courseDao);
        return courseDao.getId();
    }

    @RequestMapping(value = "/ref", method = RequestMethod.POST)
    @ResponseBody
    public String createRef(@RequestBody Map<String, List<Integer>> refMap,
                            @RequestParam(name = "courseId") Integer courseId,
                            @RequestParam(name = "orgId") Integer orgId) {
        for (String key : refMap.keySet()) {
            InsertRefsHandler insertRefsHandler = insertRefsHandlerMap.get(key);
            if (insertRefsHandler == null) {
                System.out.println("key = " + key + " doesn't has a handler");
                continue;
            }
            insertRefsHandler.insert(orgId, courseId, refMap.get(key));
        }
        return "success";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    @ResponseBody
    public CourseDao search(@RequestParam(name = "id") Integer id) {
        return courseService.obtainCourseById(id);
    }

    @RequestMapping(value = "/list/", method = RequestMethod.GET)
    @ResponseBody
    public List<CourseDao> list(@RequestParam(name = "pageNum", defaultValue = "0") Integer pageNum,
                                @RequestParam(name = "pageSize", defaultValue = "10") Integer pageSize,
                                @RequestParam(name = "orgId") Integer orgId) {
        return courseService.listCourse(pageNum, pageSize, orgId);
    }
}

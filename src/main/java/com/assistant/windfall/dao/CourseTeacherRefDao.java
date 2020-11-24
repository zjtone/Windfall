package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CourseTeacherRefDao extends Dao{
    protected Integer id;
    protected Integer courseId = -1;
    protected Integer teacherId = -1;

    public CourseTeacherRefDao(Integer courseId, Integer teacherId, Integer orgId) {
        this.courseId = courseId;
        this.teacherId = teacherId;
        this.orgId = orgId;
    }
}

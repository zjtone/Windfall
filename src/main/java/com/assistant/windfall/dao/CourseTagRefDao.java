package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CourseTagRefDao extends Dao{
    protected Integer id;
    protected Integer courseId = -1;
    protected Integer tagId = -1;

    public CourseTagRefDao(){}

    public CourseTagRefDao(Integer courseId, Integer tagId, Integer orgId){
        this.courseId = courseId;
        this.tagId = tagId;
        this.orgId = orgId;
    }
}

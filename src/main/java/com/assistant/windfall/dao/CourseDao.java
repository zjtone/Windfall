package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CourseDao extends Dao{
    private Integer id;
    private String name;
    private String description;
    private String img;

    @Override
    public String toString() {
        return "CourseDao{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", img='" + img + '\'' +
                ", orgId=" + orgId +
                '}';
    }
}

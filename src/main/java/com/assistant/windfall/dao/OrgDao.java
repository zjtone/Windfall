package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;
import org.apache.ibatis.annotations.Options;

@Getter
@Setter
public class OrgDao {
    private Integer id;
    private String name;
    private String description;
    private String email;
    private String password;
    private int status;
}

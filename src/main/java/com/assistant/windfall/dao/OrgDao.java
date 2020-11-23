package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class OrgDao extends Dao{
    private Integer id;
    private String name;
    private String description;
    private String email;
    private String password;
}

package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserDao extends People{
    protected Integer parentId = -1;
}
